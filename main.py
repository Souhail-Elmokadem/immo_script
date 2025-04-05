import threading
from scrapers.agenZ.agenz_location_scraper import AgenZLocationScraper
from scrapers.avito_immo.avito_immo_scraper import AvitoImmoScraper
from scrapers.mubawab.mubawab_scraper import MubawabScraper
from scrapers.sarouty.sarouty_location_scraper import SaroutyLocationScraper
from scrapers.yakeey.yakeey_location_scraper import YakeeyLocationScraper
from scrapers.yakeey.yakeey_scraper import YakeeyScraper
from scrapers.sarouty.sarouty_scraper import SaroutyScraper
from scrapers.agenZ.agenz_scraper import AgenZScraper
from scrapers.mubawab.mubawab_scraper_location import MubawabLocationScraper
from database.db_manager import create_database_if_not_exists, create_immobilier_table
from config import DB_CONFIG

import time

# Un dictionnaire global pour suivre l’état des scrapers
scraper_status = {}

def run_scraper(scraper_instance):
    name = scraper_instance.__class__.__name__
    scraper_status[name] = "⏳ En cours..."
    print(f"🚀 Lancement de: {name}")
    try:
        scraper_instance.scrape()
        scraper_status[name] = "✅ Terminé"
    except Exception as e:
        scraper_status[name] = f"❌ Échec: {str(e)}"
    print(f"🛑 Fin de: {name}")

def monitor_status():
    while any(status == "⏳ En cours..." for status in scraper_status.values()):
        print("\n🩺 État des scrapers :")
        for name, status in scraper_status.items():
            print(f" - {name}: {status}")
        time.sleep(5)  # Vérifie toutes les 5 secondes

if __name__ == "__main__":
    create_database_if_not_exists(DB_CONFIG["database"])
    create_immobilier_table()

    scrapers = [
        # AvitoImmoScraper(),
        #    MubawabScraper(),
          MubawabLocationScraper()
        #  YakeeyScraper(),
        # YakeeyLocationScraper(),
        #    SaroutyScraper()
        # SaroutyLocationScraper()
        #   AgenZScraper()
        # AgenZLocationScraper()
    ]

    threads = []

    # Démarrer les scrapers
    for scraper in scrapers:
        thread = threading.Thread(target=run_scraper, args=(scraper,))
        threads.append(thread)
        thread.start()

    # Démarrer le thread de monitoring
    monitor_thread = threading.Thread(target=monitor_status)
    monitor_thread.start()

    # Attendre la fin des scrapers
    for thread in threads:
        thread.join()

    # Une fois tous terminés, afficher le résultat final
    print("\n✅ Tous les scrapers ont terminé.")
    print("🧾 Résumé final :")
    for name, status in scraper_status.items():
        print(f" - {name}: {status}")
