from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
import html  # Keep this module!
import time
import requests

def fetch_page_with_selenium(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(2)  # Wait for dynamic content
    page_source = driver.page_source  # 👈 renamed this from `html` to `page_source`
    driver.quit()
    return page_source

def extract_phone_number(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    scripts = soup.find_all("script")
    adresse = soup.find_all("p", class_="MuiTypography-root MuiTypography-body1 neighborhoodname mui-b2zo6g")
    ville = soup.find_all("p", class_="MuiTypography-root MuiTypography-body1 cityname mui-b2zo6g")
    
    print(f"🏠 Adresse: {adresse[0].text.strip() if adresse else 'No Adresse'} ville: {ville[0].text.strip() if ville else 'No Ville'}")
    adresseClean = adresse[0].text.strip()+" "+ ville[0].text.strip() if adresse else None
    
    latitude, longitude = geocode_address(adresseClean) if adresseClean else (None, None)
    phone = None
    for script in scripts:
        if script.string and 'phoneNumber' in script.string:
            
            # Now html.unescape works fine
            clean_script = html.unescape(script.string).replace("\\", "")
            
            match = re.search(r'"phoneNumber"\s*:\s*"?(212\d+)', clean_script)
            if match:
                phone = match.group(1)
    return {
        "phone": phone,
        "address": adresseClean,
        "latitude": latitude,
        "longitude": longitude
        } 
    return None

def geocode_address(address):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"},timeout=10)
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        print(f"❌ Geocoding failed: {e}")
    return None, None

def getinfo_from_listing(url):
    page_html = fetch_page_with_selenium(url)
    
    return extract_phone_number(page_html)

  
