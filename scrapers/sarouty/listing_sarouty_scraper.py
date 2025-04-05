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
        # 🔧 Corriger l'URL si elle est mal formée
        cleaned_url = re.sub(r"https://www\.sarouty\.mahttps:", "https:", url)

        response = requests.get(cleaned_url, headers=headers)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # 📞 Téléphone
        phone_match = re.search(r'"phone":\{"type":"phone","value":"(\+212\d+)"', html)
        phone = phone_match.group(1) if phone_match else None

        # 🏢 Développeur
        developer = None
        societe_tag = soup.find("div", string="Société:")
        if societe_tag:
            dev_tag = societe_tag.find_next("div", class_="agent-info__detail-content--bold")
            if dev_tag:
                developer = dev_tag.text.strip()

        # 🌍 Coordonnées géographiques
        lat_match = re.search(r'"lat":([0-9.]+)', html)
        lon_match = re.search(r'"lon":(-?[0-9.]+)', html)
        latitude = float(lat_match.group(1)) if lat_match else None
        longitude = float(lon_match.group(1)) if lon_match else None

        # 🖼️ Images
        image_urls = []
        for img in soup.find_all("img"):
            src = img.get("src")
            if src and "/property/" in src:
                image_urls.append(src)
        images_string = ",".join(image_urls)

        # 📝 Description (avec fallback si absente)
        description_div = soup.find("div", class_=re.compile("property-description__text-trim"))
        if description_div:
            description = description_div.get_text(separator="\n").strip()
        else:
            print(f"⚠️ Aucune description trouvée pour: {url}")
            description = ""

        return {
            "phone": phone,
            "developer": developer,
            "latitude": latitude,
            "longitude": longitude,
            "images": images_string,
            "description": description
        }

    except requests.RequestException as e:
        print(f"❌ Error fetching listing page: {e}")
        return {
            "phone": None,
            "developer": None,
            "latitude": None,
            "longitude": None,
            "images": "",
            "description": ""
        }
