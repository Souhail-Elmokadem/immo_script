# scrapers/yakeey_scraper.py
import numbers
from models.immobilier import Immobilier
from ..base_scraper import BaseScraper
from bs4 import BeautifulSoup
from database.db_manager import save_to_database_immo
import re
from utils.utils import Utils
class MubawabScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://www.mubawab.ma/fr/sc/appartements-a-vendre", "page")

    def parse_page(self, html):
        baseUrl = "https://www.mubawab.ma"

        soup = BeautifulSoup(html, "html.parser")
        print(f"🔍 Parsing page:")
        posts = soup.find_all("div",{"class":"listingBox"})


        print(f"🔍 Found {len(posts)} posts on page")
     
        # for p in posts:
        #     try:
        #         title_tag = p.find("h2", class_="listingTit col-11")
        #         title = title_tag.text.strip() if title_tag else "No Title"

        #         infos = p.find_all("div", {'class': 'adDetailFeature'})
                
                
        #         # otherinfos = p.find_all("p", {'class': 'MuiTypography-root MuiTypography-body1 mui-18igfzf'})

        #         imageList  = p.find_all("img", {'class': 'sliderImage'})
        #         imagesString = ""
        #         for img in imageList:
        #             imagesString += img['data-lazy'] + ","
        #             print(f"🖼️ Image: {img['data-lazy']}")

        #         # surface, chambres, salles_de_bains = extract_property_info(otherinfos)

        #         surface = infos[0].text.strip() if len(infos) > 0 else "No Title"
        #         piece = infos[1].text.strip() if len(infos) > 1 else "No Price"


        #         ville_tag = p.find("span", class_="listingH3")
        #         ville = ville_tag.text.strip() if ville_tag else "No Ville"

        #         price = p.find("span", class_="priceTag ")
        #         price = price.text.strip() if price else "No Price"

        #         listing_url_tag = p.find("a")['href']


        #         complete_url = f"{listing_url_tag}"
        #         price_numeric = Utils.get_numeric_value(price)

                
        #         price_en_m2 = Utils.safe_division(price, surface)
                


        #         immobilier = Immobilier(
        #             titre=title,
        #             prix=price_numeric,
        #             url=complete_url,
        #             images_urls=imagesString,
        #             ville=ville,
        #             balcon=1,
        #             # surface_totale_m2=surface,
        #             prix_en_m2=price_en_m2,
        #             # chambres=chambres,
        #             # longitude=details.get("longitude"),
        #             # latitude=details.get("latitude"),
        #             # contact_phone=details.get("phone"),
        #             # salles_de_bains=salles_de_bains,
        #             concierge=1,
        #             # developer="",
        #             source="Yakeey"
        #         )

        #         print(f"✅ Data Parsed: {title} - {price}")
        #         # save_to_database_immo(immobilier)

        #     except Exception as e:
        #         print(f"❌ Error parsing data: {e}, skipping...")
        #         continue
