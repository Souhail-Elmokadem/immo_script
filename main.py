# main.py
from scrapers.avito_immo.avito_immo_scraper import AvitoImmoScraper
from scrapers.yakeey.yakeey_scraper import YakeeyScraper
from scrapers.sarouty.sarouty_scraper import SaroutyScraper
if __name__ == "__main__":
    scrapers = [
        # AvitoScraper(),
        # AvitoImmoScraper(),
        # YakeeyScraper()
        SaroutyScraper()
        # Add more scrapers here later
    ]

    for scraper in scrapers:
        scraper.scrape()
