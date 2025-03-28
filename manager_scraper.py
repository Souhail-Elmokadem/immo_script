# scraper_manager.py
from threading import Thread
from typing import Dict
from scrapers.avito_immo.avito_immo_scraper import AvitoImmoScraper
from scrapers.mubawab.mubawab_scraper import MubawabScraper
from scrapers.yakeey.yakeey_scraper import YakeeyScraper
from scrapers.sarouty.sarouty_scraper import SaroutyScraper
from scrapers.agenZ.agenz_scraper import AgenZScraper

scraper_classes = {
    "avito": AvitoImmoScraper,
    "mubawab": MubawabScraper,
    "yakeey": YakeeyScraper,
    "sarouty": SaroutyScraper,
    "agenz": AgenZScraper
}

threads: Dict[str, Thread] = {}
scraper_status: Dict[str, str] = {}

def run_scraper(name: str):
    scraper_status[name] = "⏳ En cours..."
    try:
        scraper = scraper_classes[name]()
        scraper.scrape()
        scraper_status[name] = "✅ Terminé"
    except Exception as e:
        scraper_status[name] = f"❌ Échec: {str(e)}"
