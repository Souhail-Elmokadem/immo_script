# scrapers/avito_scraper.py
from .base_scraper import BaseScraper
from bs4 import BeautifulSoup
from database.db_manager import save_to_database

class AvitoScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://www.avito.ma/fr/maroc/immobilier","o")

    def parse_page(self, html):
        """Parse Avito page and extract data"""
        soup = BeautifulSoup(html, "html.parser")
        posts = soup.find_all("a", class_="sc-1jge648-0 jZXrfL")

        for p in posts:
            title_tag = p.find("p", class_="sc-1x0vz2r-0 iHApav")
            price_tag = p.find("p", class_="sc-1x0vz2r-0 dJAfqm sc-b57yxx-3 eTHoJR")
            time_tag = p.find("p", class_="sc-1x0vz2r-0 layWaX")

            title = title_tag.text.strip() if title_tag else "No Title"
            price = price_tag.text.strip() if price_tag else "No Price"
            time = time_tag.text.strip() if time_tag else "No Time"

            listing_url = p["href"] if p.has_attr("href") else "No URL Found"

            print(f"Title: {title}, Price: {price}, Time: {time}, URL: {listing_url}")
            save_to_database(title, time, price, listing_url)
