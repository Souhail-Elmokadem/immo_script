from models.immobilier import Immobilier
from ..standard_base.base_standard import BaseScraper
from bs4 import BeautifulSoup
from database.db_manager import save_to_database_immo
from scrapers.sarouty.listing_sarouty_scraper import get_listing_info
from utils.utils import Utils
import re

class SaroutyLocationScraper(BaseScraper):
    def __init__(self):
        super().__init__(
            "https://www.sarouty.ma/louer/proprietes-a-vendre.html",
            "page",
        )

    def parse_page(self, html):
        baseUrl = "https://www.sarouty.ma"
        soup = BeautifulSoup(html, "html.parser")
        posts = soup.find_all("div", class_="card-list__item")
        print(f"🔍 Found {len(posts)} listings")

        def get_item_text(items, index):
            try:
                return items[index].contents[1].text.strip()
            except:
                return None

        for p in posts:
            try:
                title_tag = p.find("h2", class_="card-intro__title")
                type_tag = p.find("p", class_="card-intro__type")
                price_tag = p.find("p", class_="card-intro__price")
                ville_tag = p.find("span", class_="card-specifications__location-text")

                if not title_tag or not price_tag:
                    continue

                title = title_tag.text.strip()
                price = price_tag.text.strip()
                type_de_bien = type_tag.text.strip() if type_tag else "N/A"
                ville = ville_tag.text.strip() if ville_tag else "No Ville"

                items = p.find_all("p", class_="card-specifications__item")
                surface = get_item_text(items, 2)
                chambres = get_item_text(items, 1)
                salles_de_bains = get_item_text(items, 0)

                listing_tag = p.find("a", class_="card__link")
                listing_url = listing_tag["href"] if listing_tag else ""
                complete_url = baseUrl + listing_url

                details = get_listing_info(complete_url)
                price_en_m2 = Utils.safe_division(price, surface)

                immobilier = Immobilier(
                    titre=title,
                    prix=Utils.get_numeric_value(price),
                    url=complete_url,
                    images_urls=details.get("images"),
                    ville=ville,
                    surface_totale_m2=Utils.get_numeric_value(surface),
                    chambres=details.get("chambres") or chambres,
                    salles_de_bains=details.get("salles_de_bains") or salles_de_bains,
                    prix_en_m2=round(price_en_m2) if price_en_m2 else 0,
                    developer=details.get("developer"),
                    contact_phone=details.get("phone"),
                    longitude=details.get("longitude"),
                    latitude=details.get("latitude"),
                    source="sarouty",
                    type_de_bien=type_de_bien,
                    type_transaction="Location",
                    description=details.get("description"),
                )

                save_to_database_immo(immobilier)

            except Exception as e:
                print(f"❌ Error parsing data: {e}, skipping...")
                continue
