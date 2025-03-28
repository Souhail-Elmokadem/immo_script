# scrapers/yakeey_scraper.py
import numbers
from models.immobilier import Immobilier
from ..standard_base.base_standard import BaseScraper
from bs4 import BeautifulSoup
from database.db_manager import save_to_database_immo
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from utils.utils import Utils
import json
class AgenZScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://agenz.ma/en/acheter", "page")


    # redifintion de la methode fetch_page
    def fetch_page(self, url):
        base_url = "https://agenz.ma"
        """Override to handle lazy loading for Mubawab"""
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_listingCard_1k4wq_1"))
            )

            # Scroll multiple times to load more results
            for _ in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

        except Exception as e:
            print(f"⚠️ Timeout or error on {url}: {e}")
            return None

        return self.driver.page_source

    def parse_page(self, html):
        base_url = "https://agenz.ma"
        def extract_full_location(line):
                    if "-" in line:
                        return line.split("-")[-1].strip()
                    return None
        
        soup = BeautifulSoup(html, "html.parser")
        
        posts = soup.find_all("div", class_="_listingCard_1k4wq_1")
        for p in posts:
            try:
                title_tag = p.find("a", class_="_locationAdress_1qcbr_192")
                title = title_tag['title'] if title_tag else "No Title"
                
                # infos = p.find_all("div", {'class': 'adDetailFeature'})
                
                
                
                image_blocks = p.find_all("div", {'class': '_imageItem_xtk0p_35'})

                # If <img> tags are inside those divs
                image_urls = []

                for div in image_blocks:
                    img = div.find("img")  # Or another tag inside
                    if img and img.get("src"):
                        imagtemp = base_url+img.get("src")
                        image_urls.append(imagtemp)

                imagesString = ",".join(image_urls)


                rooms_info = p.find_all("div", class_="_rooms_1qcbr_139")

                surface = chambres = salles_de_bains = None

                for block in rooms_info:
                    value_tag = block.find("div", class_="_nouveau_1qcbr_60")
                    label_tag = block.find("div", class_="_typeBien_1qcbr_148")

                    if not value_tag or not label_tag:
                        continue

                    value = value_tag.text.strip()
                    label = label_tag.text.strip().lower()

                    if "bedroom" in label:
                        chambres = value
                    elif "bathroom" in label:
                        salles_de_bains = value
                    elif "sqm" in label:
                        surface = value

                
               
                
                ville = extract_full_location(title)
                
                price = p.find("span", class_="_nouveau_1qcbr_60")
                price = price.text.strip() if price else "No Price"
                listing_url_tag = p.find("a")
                if listing_url_tag and listing_url_tag.has_attr('href'):
                    listing_url = listing_url_tag.get("href")
                else:
                    listing_url = "No URL"


                complete_url = f"{base_url}{listing_url}"
                price_numeric = Utils.get_numeric_value(price)

                
                price_en_m2 = Utils.safe_division(price, surface)
                
                long,lat = Utils.geocode_address(ville)



                immobilier = Immobilier(
                    titre=title,
                    prix=price_numeric,
                    url=complete_url,
                    images_urls=imagesString,
                    ville=ville,
                    balcon=1,
                    surface_totale_m2=Utils.get_numeric_value(surface),
                     prix_en_m2=price_en_m2,
                    chambres=Utils.get_numeric_value(chambres),
                    longitude=long if long else 0,
                    latitude=lat if lat else 0,
                    # contact_phone=details.get("phone"),
                    salles_de_bains=Utils.get_numeric_value(salles_de_bains),
                    concierge=1,
                    # developer="",
                    source="Agenz"
                )

                if title == "No Title" or price_numeric == 0:
                    continue
                save_to_database_immo(immobilier)

            except Exception as e:
                print(f"❌ Error parsing data: {e}, skipping...")
                continue


