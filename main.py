# main.py
from scrapers.avito_immo.avito_immo_scraper import AvitoImmoScraper
from scrapers.mubawab.mubawab_scraper import MubawabScraper
from scrapers.yakeey.yakeey_scraper import YakeeyScraper
from scrapers.sarouty.sarouty_scraper import SaroutyScraper
from scrapers.agenZ.agenz_scraper import AgenZScraper
from database.db_manager import create_database_if_not_exists, create_immobilier_table
from config import DB_CONFIG
if __name__ == "__main__":
    
    
    create_database_if_not_exists(DB_CONFIG["database"])
    create_immobilier_table()
    
    scrapers = [
        # AvitoScraper(),
        #  AvitoImmoScraper(),
            # YakeeyScraper(),
            #  MubawabScraper()
            # SaroutyScraper()
            AgenZScraper()
        # Add more scrapers here later
    ]

    for scraper in scrapers:
        scraper.scrape()
