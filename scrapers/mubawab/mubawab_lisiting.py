from bs4 import BeautifulSoup
import requests

class Mubawab_listing:

    @staticmethod
    def get_coordinates_from_listing(url):
        try:
            response = requests.get(url, timeout=15)
            if response.status_code != 200:
                return 0, 0

            soup = BeautifulSoup(response.text, "html.parser")
            map_div = soup.find("div", id="mapOpen")

            if map_div:
                lat = map_div.get("lat")
                lon = map_div.get("lon")
                return float(lon), float(lat)
            else:
                return 0, 0
        except Exception as e:
            print(f"❌ Error fetching coordinates from {url}: {e}")
            return 0, 0

    @staticmethod
    def extract_images_from_listing(url):
        try:
            response = requests.get(url, timeout=15)
            if response.status_code != 200:
                print(f"❌ Failed to load listing page: {url}")
                return []

            soup = BeautifulSoup(response.text, "html.parser")

            # Récupère toutes les images depuis les balises img avec un attribut src
            image_tags = soup.find_all("img", src=True)
            # Filtrer uniquement les URLs d'images Mubawab
            image_urls = [img['src'] for img in image_tags if "mubawab-media.com" in img['src']]

            return image_urls

        except Exception as e:
            print(f"❌ Error extracting images from listing: {e}")
            return []
    @staticmethod
    def get_description_from_listing(url):
        try:
            response = requests.get(url, timeout=15)
            soup = BeautifulSoup(response.text, "html.parser")

            # Chercher le premier <div class="blockProp">
            block = soup.find("div", class_="blockProp")
            if not block:
                return None

            # Récupérer le premier paragraphe
            paragraph = block.find("p")
            if not paragraph:
                return None

            # Nettoyer tous les <br> et récupérer le texte complet
            description = paragraph.get_text(separator="\n").strip()
            return description

        except Exception as e:
            print(f"❌ Error getting description: {e}")
            return None


    @staticmethod
    def get_type_de_bien_from_listing(url):
        try:
            response = requests.get(url, timeout=15)
            soup = BeautifulSoup(response.text, "html.parser")

            labels = soup.find_all("p", class_="adMainFeatureContentLabel")
            for label in labels:
                if "Type de bien" in label.text:
                    value = label.find_next_sibling("p", class_="adMainFeatureContentValue")
                    return value.text.strip() if value else None
            return None
        except Exception as e:
            print(f"❌ Error extracting type de bien: {e}")
            return None
