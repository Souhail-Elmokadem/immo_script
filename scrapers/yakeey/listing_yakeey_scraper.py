import requests
import json
from bs4 import BeautifulSoup
import re

def get_listing_info(url):
    """
    Extract listing details from the webpage, find `userRef`, and fetch latitude & longitude from API.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com",
    }
    try:
        
        cleaned_url = re.sub(r"https://www\.sarouty\.mahttps:", "https:", url)
        print(cleaned_url)
        response = requests.get(cleaned_url,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        images = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                if "/property/" in src: 
                    images.append(src)
        print(images)
        imgesString = ""
        for i in images:
            imgesString = imgesString+","+i
        return imgesString

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching listing page: {e}")
        return None, None



