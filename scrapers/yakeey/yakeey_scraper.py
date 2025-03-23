# scrapers/yakeey_scraper.py
import numbers
from models.immobilier import Immobilier
from ..base_scraper import BaseScraper
from bs4 import BeautifulSoup
from database.db_manager import save_to_database_immo
import re
from utils.utils import Utils
from scrapers.yakeey.listing_yakeey_scraper import getinfo_from_listing
class YakeeyScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://yakeey.com/fr-ma/achat/biens/maroc", "page")

    def parse_page(self, html):
        baseUrl = "https://yakeey.com"

        soup = BeautifulSoup(html, "html.parser")
        posts = soup.find_all("div", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-lg-6 MuiGrid-grid-xl-4 mui-lvpef6")

        def extract_property_info(otherinfos):
            surface = chambres = salles_de_bains = None

            if len(otherinfos) > 0:
                surface_match = re.search(r'(\d+)', otherinfos[0].text.strip())
                surface = int(surface_match.group(1)) if surface_match else None

            if len(otherinfos) > 1:
                chambres_match = re.search(r'(\d+)', otherinfos[1].text.strip())
                chambres = int(chambres_match.group(1)) if chambres_match else None

            if len(otherinfos) > 2:
                salles_de_bains_match = re.search(r'(\d+)', otherinfos[2].text.strip())
                salles_de_bains = int(salles_de_bains_match.group(1)) if salles_de_bains_match else None

            return surface, chambres, salles_de_bains

        def reformat_yakeey_url(url):
            match = re.search(r"/cdn-cgi/image/[^/]+/(.+)$", url)
            if match:
                return f"https://medias.yakeey.com/cdn-cgi/image/width=/{match.group(1)}"
            return url  # fallback

        for p in posts:
            try:
                title_tag = p.find("p", class_="MuiTypography-root MuiTypography-body1 mui-1pel3ec")
                title = title_tag.text.strip() if title_tag else "No Title"

                infos = p.find_all("p", {'class': 'MuiTypography-root MuiTypography-body1 mui-1pe1e3c'})
                otherinfos = p.find_all("p", {'class': 'MuiTypography-root MuiTypography-body1 mui-18igfzf'})

                imageList  = p.find_all("img", {'class': 'property-card-image MuiBox-root mui-0'})
                imagesString = ""
                for img in imageList:
                    imagesString += reformat_yakeey_url(img['src']) + ","
                    print(f"🖼️ Image: {reformat_yakeey_url(img['src'])}")

                surface, chambres, salles_de_bains = extract_property_info(otherinfos)

                title = infos[0].text.strip() if len(infos) > 0 else "No Title"
                price = infos[1].text.replace("•", "").strip() if len(infos) > 1 else "No Price"

                if price == "No Price":
                    price_tag = p.find("p", class_="MuiTypography-root MuiTypography-body1 mui-f6ygni") or p.find("span", class_="MuiBox-root mui-111t5zu")
                    price = price_tag.text.strip() if price_tag else "No Price"

                ville_tag = p.find("p", class_="MuiTypography-root MuiTypography-body1 mui-17qqh56")
                ville = ville_tag.text.strip() if ville_tag else "No Ville"

                listing_url_tag = p.find("a", {'class': 'MuiBox-root mui-1y4n71p'})
                if listing_url_tag and "href" in listing_url_tag.attrs:
                    listing_url = listing_url_tag["href"]
                else:
                    print("⚠️ Listing URL not found, skipping...")
                    continue

                complete_url = f"{baseUrl}{listing_url}"
                # categ = extract_phone_from_url(complete_url)
                # print(f"📞 Phone: {categ}")
                # if not categ:
                #     print(f"⚠️ Phone not found for {complete_url}, skipping...")
                    

                price_numeric = Utils.get_numeric_value(price)

                
                price_en_m2 = Utils.safe_division(price, surface)
                details = getinfo_from_listing(complete_url)


                immobilier = Immobilier(
                    titre=title,
                    prix=price_numeric,
                    url=complete_url,
                    images_urls=imagesString,
                    ville=ville,
                    balcon=1,
                    surface_totale_m2=surface,
                    prix_en_m2=price_en_m2,
                    chambres=chambres,
                    longitude=details.get("longitude"),
                    latitude=details.get("latitude"),
                    contact_phone=details.get("phone"),
                    salles_de_bains=salles_de_bains,
                    concierge=1,
                    # developer="",
                    source="Yakeey"
                )

                print(f"✅ Data Parsed: {title} - {price}")
                save_to_database_immo(immobilier)

            except Exception as e:
                print(f"❌ Error parsing data: {e}, skipping...")
                continue
