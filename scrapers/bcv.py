import httpx
from selectolax.parser import HTMLParser
from logs_config import logger
from .base import BaseScraper

class BCVScrapper(BaseScraper):
    def __init__(self, selector: str):
        self.url = "https://www.bcv.org.ve/"
        self.selector = selector
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,webp,*/*;q=0.8",
        }
    
    def extract(self) -> float:
        try:
            with httpx.Client(verify=False, timeout=30.0) as client:
                logger.info(f"Conectando a {self.url}...")
                response = client.get(self.url, headers=self.headers)
                response.raise_for_status()

            tree = HTMLParser(response.text)
            node = tree.css_first(self.selector)

            if not node:
                raise ValueError(f"Selector: ({self.selector}) not found")
            
            clean_value = node.text().strip().replace(',', '.')

            return float(clean_value)
        except httpx.HTTPError as e:
            logger.error(f"Network error with BCV: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error on BCVScraper: {e}")
            raise