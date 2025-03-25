import requests
import time

# Liste des adresses extraites de ton fichier ou texte
adresses = [
    "DERB BACHKOU ROUTE 109 COMMUNE MAARIF CASABLANCA",
]

# Fonction pour géocoder une adresse via Nominatim
def get_coordinates(address):
    url = f"https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    try:
        response = requests.get(url, params=params, headers={"User-Agent": "geo-script"})
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            return None, None
    except Exception as e:
        print(f"❌ Erreur pour '{address}': {e}")
        return None, None

# Boucle sur les adresses
for adresse in adresses:
    lat, lon = get_coordinates(adresse)
    print(f"📍 {adresse} → Latitude: {lat}, Longitude: {lon}")
    time.sleep(1)  # Pause pour respecter le service (important pour Nominatim)
