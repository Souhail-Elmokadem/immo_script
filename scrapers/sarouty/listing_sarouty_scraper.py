import requests
import json
from bs4 import BeautifulSoup


def get_listing_info(url):
    """
    Extract listing details from the webpage, find `userRef`, and fetch latitude & longitude from API.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the `userRef` (Look for a unique identifier in scripts)
        script_tags = soup.find_all("div", {'class':'MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-4 MuiGrid-grid-md-4 MuiGrid-grid-lg-4 mui-qb781s'})
        print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
        for i in script_tags:
            print(i.text.strip())
        
        return script_tags

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching listing page: {e}")
        return None, None



def extract_lat_lon(address):
    
    if not address:
        return None, None
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data:
            return data[0]["lat"], data[0]["lon"]
        
    except Exception as e:
        print(f"⚠️ Error fetching location: {e}")

    return None, None
