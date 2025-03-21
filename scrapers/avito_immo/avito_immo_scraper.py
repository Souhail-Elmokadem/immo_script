
# scrapers/avito_scraper.py
import numbers
from models.immobilier import Immobilier
from ..base_scraper import BaseScraper
from bs4 import BeautifulSoup
from database.db_manager import  save_to_database_immo
import re
from scrapers.avito_immo.listing_avito_immo_scraper import get_listing_info

from utils.utils import Utils
class AvitoImmoScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://immoneuf.avito.ma/fr/s/maroc","page")

    def parse_page(self, html):
        baseUrl = "https://immoneuf.avito.ma"

        """Parse Avito page and extract data"""
        soup = BeautifulSoup(html, "html.parser")
        posts = soup.find_all("a", class_="sc-1jge648-0 jZXrfL")

        def get_item_text( items, index):
            """Safely extract text from items list."""
            return items[index].contents[1].text.strip() if len(items) > index else None


        for p in posts:
            title_tag = p.find("p", class_="sc-1x0vz2r-0 iHApav")
            price_tag = p.find("p", class_="sc-1x0vz2r-0 dJAfqm sc-b57yxx-3 eTHoJR")
            time_tag = p.find("p", class_="sc-1x0vz2r-0 layWaX")
            ville_tag = p.find("p", class_="sc-1x0vz2r-0 layWaX")
            items = p.find_all("span",{'class':'sc-1s278lr-0 cAiIZZ'})
            title = title_tag.text.strip() if title_tag else "No Title"
            price = price_tag.text.strip() if price_tag else "No Price"
            time = time_tag.text.strip() if time_tag else "No Time"
            ville = ville_tag.text.strip() if ville_tag else "No Ville"
            listing_url = p["href"] if p.has_attr("href") else "No URL Found"

            details = get_listing_info(f"https://immoneuf.avito.ma{listing_url}")
            if details is None:
                        print(f"❌ Failed to extract details for: {title} ({listing_url})")
                        continue  # Skip this entry and proceed with the next

            print("-+-----------------")
            if details:
                print("\n✅ Extracted Project Info:")
                for key, value in details.items():
                    print(f"{key}: {value}")
            print("-+-----------------")

       
            
            surface_totale = get_item_text(items, 0)
            chambres = get_item_text(items, 1)
            salles_de_bains = get_item_text(items, 2)

            

            price_en_m2 = None
            if(isinstance(Utils.get_numeric_value(price),numbers.Number)):
                print(Utils.get_numeric_value(price))
                price_en_m2=Utils.get_numeric_value(price)/Utils.get_numeric_value(surface_totale)
            print(price_en_m2)


            print(f"Title: {title}, Price: {price}, Time: {time}, URL: {listing_url}")
            completion_date = details.get("Completion Date", "N/A")
            developer = details.get("Developer", "N/A")
            contact_phone = details.get("Contact Phone", "N/A")

            immobilier = Immobilier(
                titre=title,
                prix=price,
                url=baseUrl+listing_url,
                ville=ville,
                surface_totale_m2=Utils.get_numeric_value(surface_totale),
                chambres=chambres,
                salles_de_bains=salles_de_bains,
                prix_en_m2=price_en_m2,
                date_d_achevement=completion_date,
                developer=developer,
                contact_phone=contact_phone,
                longitude=details.get("Longitude", None),   # Add longitude
                latitude=details.get("Latitude", None),  
                source="Avito Immobilier"
            )

            # Save to the database
            save_to_database_immo(immobilier)
            

