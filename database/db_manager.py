# database/db_manager.py
import pymysql
from config import DB_CONFIG
from models.immobilier import Immobilier

def save_to_database(title, time, price, url):
    """Saves scraped data to the database"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO listings (title, time, price, url) VALUES (%s, %s, %s, %s)", 
                       (title, time, price, url))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Saved: {title} - {price}")
    except Exception as e:
        print(f"❌ Database Error: {e}")




def save_to_database_immo(immobilier):
    """Save the Immobilier object into the database."""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """
        INSERT INTO immobilier (titre, prix, url,images_urls, latitude, longitude, balcon, concierge, ville, 
                              surface_totale_m2, salles_de_bains, chambres, source, prix_en_m2,
                              date_d_achevement, developer, contact_phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """

        cursor.execute(query, (
            immobilier.titre, immobilier.prix, immobilier.url,immobilier.images_urls, immobilier.latitude, immobilier.longitude,
            immobilier.balcon, immobilier.concierge, immobilier.ville, immobilier.surface_totale_m2,
            immobilier.salles_de_bains, immobilier.chambres, immobilier.source, immobilier.prix_en_m2,
            immobilier.date_d_achevement, immobilier.developer, immobilier.contact_phone
        ))

        conn.commit()
        cursor.close()
        conn.close()

        print(f"✅ Data Saved: {immobilier.titre} - {immobilier.prix}")

    except Exception as e:
        print(f"❌ Database Error: {e}")