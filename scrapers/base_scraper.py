# scrapers/base_scraper.py
from abc import ABC, abstractmethod
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseScraper(ABC):
    def __init__(self, base_url,params):
        self.base_url = base_url
        self.params = params
        self.driver = webdriver.Chrome()

    @abstractmethod
    def parse_page(self, html):
        """Extract data from a page (Implemented in child classes)"""
        pass
  
    def fetch_page(self, url):
        """Fetch page source using Selenium"""
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 20).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        except Exception:
            print(f"⚠️ Warning: Page load timeout on {url}")
        return self.driver.page_source

    def scrape(self, max_pages=100):
        """Main scraping loop"""
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}?{self.params}={page}"
            print(f"Scraping {url}...")
            html = self.fetch_page(url)
            self.parse_page(html)
