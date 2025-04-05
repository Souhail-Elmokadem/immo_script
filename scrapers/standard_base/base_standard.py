from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

class BaseScraper(ABC):
    def __init__(self, base_url, params, scroll_selector=None):
        self.base_url = base_url
        self.params = params
        self.scroll_selector = scroll_selector  # class or selector used to wait for scroll
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=options)

    @abstractmethod
    def parse_page(self, html):
        """Extract data from a page (Implemented in child classes)"""
        pass

    def fetch_page(self, url):
        self.driver.get(url)

        try:
            if self.scroll_selector:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, self.scroll_selector))
                )

            for _ in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

            time.sleep(5)  # force JS lazy load to complete
        except Exception as e:
            print(f"⚠️ Scroll or load error: {e}")

        return self.driver.page_source


    def scrape(self, max_pages=100):
        """Main scraping loop"""
        try:
            for page in range(1, max_pages):
                url = f"{self.base_url}?{self.params}={page}"
                print(f"Scraping {url}...")
                html = self.fetch_page(url)
                if html:
                    self.parse_page(html)
        finally:
            print("🧹 Quitting WebDriver...")
            self.driver.quit()
