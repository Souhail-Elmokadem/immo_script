
# scrapers/avito_scraper.py
import numbers
from models.immobilier import Immobilier
from ..base_scraper import BaseScraper
from bs4 import BeautifulSoup
from database.db_manager import  save_to_database_immo
import re

from scrapers.yakeey.listing_yakeey_scraper import extract_phone_from_url

from utils.utils import Utils
class YakeeyScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://yakeey.com/fr-ma/achat/biens/maroc","page")

    def parse_page(self, html):
        baseUrl = "https://yakeey.com"

        """Parse Avito page and extract data"""
        soup = BeautifulSoup(html, "html.parser")
        posts = soup.find_all("div", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-lg-6 MuiGrid-grid-xl-4 mui-lvpef6")

        def get_item_text( items, index):
            """Safely extract text from items list."""
            return items[index].contents[1].text.strip() if len(items) > index else None

        def extract_property_info(otherinfos):
            """Extract surface, bedrooms, and bathrooms from the list of elements"""
            
            surface = None
            chambres = None
            salles_de_bains = None

            if len(otherinfos) > 0:
                surface = otherinfos[0].text.strip().split(" ")[0] if "m²" in otherinfos[0].text else None
            
            if len(otherinfos) > 1:
                chambres_text = otherinfos[1].text.strip()
                chambres = re.search(r"(\d+)", chambres_text)  # Extraire le nombre
                chambres = int(chambres.group(1)) if chambres else None

            if len(otherinfos) > 2:
                salles_de_bains_text = otherinfos[2].text.strip()
                salles_de_bains = re.search(r"(\d+)", salles_de_bains_text)  # Extraire le nombre
                salles_de_bains = int(salles_de_bains.group(1)) if salles_de_bains else None

            return surface, chambres, salles_de_bains

            # def fetch_data(self, page_number=0):
            #         params = {
            #             "pageNumber": page_number,
            #             "pageSize": self.page_size,
            #             "sortBy": "listedAt",
            #             "sortDir": "DESC",
            #             "categories": "FLAT",
            #             "minPrice": self.min_price,
            #             "maxPrice": self.max_price,
            #         }

            #         try:
            #             response = requests.get(self.BASE_URL, params=params)
            #             response.raise_for_status()  # Raise exception for HTTP errors
            #             return response.json()
            #         except requests.exceptions.RequestException as e:
            #             print(f"❌ Error fetching data: {e}")
            #             return None

        # def extract_location(self, main_address):
        #             """
        #             Extracts latitude and longitude from address using OpenStreetMap API.
        #             """
        #             if not main_address:
        #                 return None, None

        #             url = f"https://nominatim.openstreetmap.org/search?format=json&q={main_address}"
        #             try:
        #                 response = requests.get(url)
        #                 data = response.json()
        #                 if data:
        #                     return data[0]["lat"], data[0]["lon"]
        #             except Exception as e:
        #                 print(f"⚠️ Error fetching location: {e}")
                    
        #             return None, None
     

        for p in posts:
            title_tag = p.find("p", class_="MuiTypography-root MuiTypography-body1 mui-1pel3ec")
            title = title_tag.text.strip() if title_tag else "No Title"




            # like title & price
            infos  = p.find_all("p",{'class':'MuiTypography-root MuiTypography-body1 mui-1pe1e3c'}) 
            

            # like surface nb chambre nb toilette
            otherinfos  = p.find_all("p",{'class':'MuiTypography-root MuiTypography-body1 mui-18igfzf'})

           

       
            print("++++++++++++++++++++++++++")
            surface, chambres, salles_de_bains = extract_property_info(otherinfos)
            

       
            title = infos[0].text.strip() if len(infos) > 0 else "No Title"
            price = infos[1].text.replace("•", "").strip() if len(infos) > 1 else "No Price"

            if price == "No Price":
                    price_tag = p.find("p", class_="MuiTypography-root MuiTypography-body1 mui-f6ygni")
                    if not price_tag:
                        price_tag = p.find("span", class_="MuiBox-root mui-111t5zu")  # Vérifier aussi les spans
                    if price_tag:
                        price = price_tag.text.strip()
          
           
        
            ville_tag = p.find("p", class_="MuiTypography-root MuiTypography-body1 mui-17qqh56")
            items = p.find_all("p",{'class':'MuiTypography-root MuiTypography-body1 mui-18igfzf'})


            



           
            # time = time_tag.text.strip() if time_tag else "No Time"
            ville = ville_tag.text.strip() if ville_tag else "No Ville"
            listing_url = p.find("a",{'class':'MuiBox-root mui-1y4n71p'})["href"] if p.find("a") else "No URL Found"

            print("+++++++++++++2+++++++++++++")
            categ = extract_phone_from_url(f"{baseUrl}{listing_url}")
            print("+++++++++++++2+++++++++++++")
            print(categ)


            price_en_m2 = None
            if price and surface:
                price_en_m2 = Utils.safe_division(price, surface)


            print(f"Title: {title}, Price: {price}, Ville: {ville}, URL: {listing_url}")
            # completion_date = details.get("Completion Date", "N/A")
            # developer = details.get("Developer", "N/A")
            # contact_phone = details.get("Contact Phone", "N/A")

            immobilier = Immobilier(
                titre=title,
                prix=Utils.get_numeric_value(price),
                url=baseUrl+listing_url,
                ville=ville,
                balcon=1 if "Ascenseur" in categ else 0,
                surface_totale_m2=surface,
                chambres=chambres,
                salles_de_bains=salles_de_bains,
                prix_en_m2=price_en_m2,
                # date_d_achevement=completion_date,
                developer=categ,
                # contact_phone=contact_phone,
                # longitude=details.get("Longitude", None),   # Add longitude
                # latitude=details.get("Latitude", None),  
                source="Yakeey"
            )

           
            save_to_database_immo(immobilier)
            

