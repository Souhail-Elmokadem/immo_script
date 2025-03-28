import requests
from bs4 import BeautifulSoup
import re

def get_listing_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com",
    }

    try:
        # Fix malformed URL if needed
        cleaned_url = re.sub(r"https://www\.sarouty\.mahttps:", "https:", url)

        response = requests.get(cleaned_url, headers=headers)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # 📞 Extract phone number using regex
        phone_match = re.search(r'"phone":\{"type":"phone","value":"(\+212\d+)"', html)
        phone = phone_match.group(1) if phone_match else None

        # 🏢 Extract developer / société
        developer = None
        societe_tag = soup.find("div", text="Société:")
        if societe_tag:
            dev_tag = societe_tag.find_next("div", class_="agent-info__detail-content--bold")
            if dev_tag:
                developer = dev_tag.text.strip()

        # 🌍 Extract latitude & longitude
        lat_match = re.search(r'"lat":([0-9.]+)', html)
        lon_match = re.search(r'"lon":(-?[0-9.]+)', html)
        latitude = float(lat_match.group(1)) if lat_match else None
        longitude = float(lon_match.group(1)) if lon_match else None

        # 🖼️ (Optional) Extract images (if you want to use it)
        image_urls = []
        for img in soup.find_all("img"):
            src = img.get("src")
            if src and "/property/" in src:
                image_urls.append(src)
        images_string = ",".join(image_urls)

        return {
            "phone": phone,
            "developer": developer,
            "latitude": latitude,
            "longitude": longitude,
            "images": images_string
        }

    except requests.RequestException as e:
        print(f"❌ Error fetching listing page: {e}")
        return None
