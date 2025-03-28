# scrapers/base_scraper.py
from abc import ABC, abstractmethod
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class BaseScraper(ABC):
    def __init__(self, base_url,params):
        self.base_url = base_url
        self.params = params
        options = Options()
        options.add_argument("--headless=new")  # Use the new headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)

    @abstractmethod
    def parse_page(self, html):
        """Extract data from a page (Implemented in child classes)"""
        pass
  
    def fetch_page(self, url):
        self.driver.get(url)
        time.sleep(5)  # Wait 5 seconds after loading the page

        try:
            WebDriverWait(self.driver, 40).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return self.driver.page_source
        except Exception:
            print(f"⚠️ Warning: Page load timeout on {url}")
            return None  # Don't quit here, let it be handled in scrape loop


    def scrape(self, max_pages=100):
        """Main scraping loop"""
        try:
            for page in range(1, max_pages + 1):
                url = f"{self.base_url}?{self.params}={page}"
                print(f"Scraping {url}...")
                html = self.fetch_page(url)
                self.parse_page(html)

        finally:
            print("🧹 Quitting WebDriver...")
            self.driver.quit()

