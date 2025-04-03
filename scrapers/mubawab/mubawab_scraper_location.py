# scrapers/yakeey_scraper.py
import numbers
from models.immobilier import Immobilier
from bs4 import BeautifulSoup
from database.db_manager import save_to_database_immo
import re

from ..base_scraper import BaseScraper
from .mubawab_lisiting  import Mubawab_listing

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from utils.utils import Utils
import json
class MubawabLocationScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://www.mubawab.ma/fr/cc/immobilier-a-louer-all:sc:apartment-rent,commercial-rent,farm-rent,house-rent,land-rent,office-rent,other-rent,riad-rent,room-rent,villa-rent:p:{}", "page")


    # redifintion de la methode fetch_page
    def fetch_page(self, url):
        """Override to handle lazy loading for Mubawab"""
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "listingBox"))
            )

            # Scroll multiple times to load more results
            for _ in range(6):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

        except Exception as e:
            print(f"⚠️ Timeout or error on {url}: {e}")
            return None

        return self.driver.page_source

    def parse_page(self, html):
        soup = BeautifulSoup(html, "html.parser")
        posts = soup.find_all("div", class_="listingBox")
        print(f"🔍 Found {len(posts)} listings on this page")

        def safe_get_info(infos, index):
            try:
                return infos[index].text.strip()
            except IndexError:
                return None

        for p in posts:
            try:
                title_tag = p.find("h2", class_="listingTit")
                title = title_tag.text.strip() if title_tag else "No Title"

                infos = p.find_all("div", {'class': 'adDetailFeature'})
                
                



                surface = safe_get_info(infos, 0)
                chambres = safe_get_info(infos, 1)
                salles_de_bains = safe_get_info(infos, 2)






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

                
                image_urls = Mubawab_listing.extract_images_from_listing(complete_url)
                imagesString = ",".join(image_urls)
                description = Mubawab_listing.get_description_from_listing(complete_url)

                price_en_m2 = Utils.safe_division(price, surface)
                
                long,lat = Mubawab_listing.get_coordinates_from_listing(complete_url)

                type_de_bien = Mubawab_listing.get_type_de_bien_from_listing(complete_url)


                immobilier = Immobilier(
                    titre=title,
                    type_transaction="Location",
                    prix=price_numeric,
                    url=complete_url,
                    type_de_bien=type_de_bien,
                    images_urls=imagesString,
                    ville=ville,
                    balcon=1,
                    surface_totale_m2=Utils.get_numeric_value(surface),
                    prix_en_m2=round(price_en_m2),
                    chambres=Utils.get_numeric_value(chambres),
                    longitude=long if long else 0,
                    latitude=lat if lat else 0,
                    description=description,
                    salles_de_bains=Utils.get_numeric_value(salles_de_bains),
                    concierge=1,
                    source="mubawab"
                )

                if  price_numeric == 0:
                    print("❌ Skipping invalid data...")
                    continue
                save_to_database_immo(immobilier)

            except Exception as e:
                print(f"❌ Error parsing data: {e}, skipping...")
                continue
    def scrape(self, max_pages=100):
        for page in range(1, max_pages):
            url = self.base_url.format(page)
            print(f"Scraping {url}...")
            html = self.fetch_page(url)
            if html:
                self.parse_page(html)

