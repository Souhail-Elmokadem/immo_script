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
class MubawabScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://www.mubawab.ma/fr/sc/appartements-a-vendre", "page")


    # redifintion de la methode fetch_page
    def fetch_page(self, url):
        """Override to handle lazy loading for Mubawab"""
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "listingBox"))
            )

            # ✅ 🔁 Nouveau scroll dynamique jusqu’à ce qu’il n’y ait plus rien à charger
            previous_height = 0
            scroll_retries = 0

            while scroll_retries < 5:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                current_height = self.driver.execute_script("return document.body.scrollHeight")

                if current_height == previous_height:
                    scroll_retries += 1
                else:
                    scroll_retries = 0
                    previous_height = current_height

        except Exception as e:
            print(f"⚠️ Timeout or error on {url}: {e}")
            return None

        return self.driver.page_source


    def parse_page(self, html):
        soup = BeautifulSoup(html, "html.parser")
        posts = soup.find_all("div", class_="listingBox")
      

        for p in posts:
            try:
                title_tag = p.find("h2", class_="listingTit col-11")
                title = title_tag.text.strip() if title_tag else "No Title"

                infos = p.find_all("div", {'class': 'adDetailFeature'})
                
                

                imageList  = p.find_all("img", {'class': 'sliderImage'})
                image_urls = [img.get("src") for img in imageList if img.get("src")]
                imagesString = (",").join(image_urls)

                
                surface = infos[0].text.strip() if len(infos) > 0 else "No Title"
                chambres = infos[2].text.strip() if len(infos) > 1 else "No Title"
                salles_de_bains = infos[3].text.strip() if len(infos) > 2 else "No Title"

                

                ville_tag = p.find("span", class_="listingH3")
                ville = ville_tag.text.strip() if ville_tag else "No Ville"
                
                price = p.find("span", class_="priceTag hardShadow float-left")
                price = price.text.strip() if price else "No Price"
                
                listing_url_tag = p.find("a")
                if listing_url_tag and listing_url_tag.has_attr('href'):
                    listing_url = listing_url_tag.get("href")
                else:
                    listing_url = "No URL"

               

                complete_url = f"{listing_url}"
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
                    source="mubawab"
                )

                if title == "No Title" or price_numeric == 0:
                    continue
                save_to_database_immo(immobilier)

            except Exception as e:
                print(f"❌ Error parsing data: {e}, skipping...")
                continue
