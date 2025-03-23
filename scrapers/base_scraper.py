# scrapers/base_scraper.py
from abc import ABC, abstractmethod
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class BaseScraper(ABC):
    def __init__(self, base_url, params):
        self.base_url = base_url
        self.params = params

    @abstractmethod
    def parse_page(self, html):
        """Extract data from a page (Implemented in child classes)"""
        pass

    def fetch_page(self, url):
        """Fetch page source using a fresh Selenium driver each time"""
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        try:
            driver.get(url)
            time.sleep(2)
            return driver.page_source
        finally:
            driver.quit()

    def scrape(self, max_pages=100):
        """Main scraping loop"""
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}?{self.params}={page}"
            print(f"Scraping {url}...")
            html = self.fetch_page(url)
            if html:
                self.parse_page(html)
