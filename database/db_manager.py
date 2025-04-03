# database/db_manager.py
import pymysql
from config import DB_CONFIG
from models.immobilier import Immobilier

def create_database_if_not_exists(db_name):
    try:
        # Connect to MySQL without selecting a database
        conn = pymysql.connect(host="localhost", user="root", password="")
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"✅ Database '{db_name}' is ready.")
        
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error creating database: {e}")

def get_connection():
        return pymysql.connect(**DB_CONFIG)

def create_immobilier_table():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS immobilier (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titre TEXT,
            prix TEXT,
            url TEXT,
            images_urls TEXT,
            latitude VARCHAR(50),
            longitude VARCHAR(50),
            balcon BOOLEAN,
            concierge BOOLEAN,
            ville TEXT,
            surface_totale_m2 VARCHAR(50),
            salles_de_bains VARCHAR(50),
            chambres VARCHAR(50),
            source TEXT,
            prix_en_m2 VARCHAR(50),
            date_d_achevement TEXT,
            developer TEXT,
            contact_phone TEXT
        )
        """
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Table 'immobilier' is ready.")
    except Exception as e:
        print(f"❌ Error creating table: {e}")




def save_to_database_immo(immobilier):
    """Save the Immobilier object into the database, if it doesn't already exist."""
    try:
       
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # ✅ Check if a record with the same URL already exists
        # cursor.execute("SELECT COUNT(*) FROM immobilier WHERE url = %s", (immobilier.url,))
        # (count,) = cursor.fetchone()

        # if count > 0:
        #     print(f"⏩ Déjà existant: {immobilier.url}")
        #     cursor.close()
        #     conn.close()
        #     return  # Skip saving

        # ✅ Insert the new record
        query = """
        INSERT INTO immobilier (titre,type_transaction ,prix, url, type_de_bien,images_urls, latitude, longitude, balcon, concierge, ville,description, 
                                surface_totale_m2, salles_de_bains, chambres, source, prix_en_m2,
                                date_d_achevement, developer, contact_phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            immobilier.titre, immobilier.type_transaction,immobilier.prix, immobilier.url, immobilier.type_de_bien, immobilier.images_urls,immobilier.latitude,
            immobilier.longitude, immobilier.balcon, immobilier.concierge, immobilier.ville,immobilier.description,
            immobilier.surface_totale_m2, immobilier.salles_de_bains, immobilier.chambres, immobilier.source,
            immobilier.prix_en_m2, immobilier.date_d_achevement, immobilier.developer, immobilier.contact_phone
        ))

        conn.commit()
        print(f"✅ Data Saved: {immobilier.titre} - {immobilier.url}")
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Database Error: {e}")


