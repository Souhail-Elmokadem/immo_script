import requests
from bs4 import BeautifulSoup
import re
import json

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def extract_json_from_script(html):
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all("script")

    for script in scripts:
        if script.string and 'window.propertyfinder.settings.moreProperties' in script.string:
            json_text_match = re.search(
                r'window\.propertyfinder\.settings\.moreProperties\s*=\s*(\{.*?\});',
                script.string,
                re.DOTALL
            )
            if json_text_match:
                json_text = json_text_match.group(1)
                try:
                    data = json.loads(json_text)
                    return data
                except json.JSONDecodeError as e:
                    print(f"JSON decoding failed: {e}")
                    return None
    return None


def get_phone_number(json_data):
    try:
        phone_number = json_data['payload']['data'][0]['meta']['contact_options']['details']['phone']['value']
        return phone_number
    except (KeyError, TypeError, IndexError) as e:
        print(f"Error extracting phone number: {e}")
        return None


def extract_phone_from_url(url):
    html = fetch_page(url)
    json_data = extract_json_from_script(html)
    if json_data:
        phone = get_phone_number(json_data)
        return phone
    return None
