from concurrent.futures import ThreadPoolExecutor
from scrapers.g2 import G2Scraper
from scrapers.capterra import CapterraScraper
from scrapers.trustradius import TrustRadiusScraper
from scrapers.hackernews import HackerNewsScraper

class ScraperManager:

    SOURCES = {
    "g2": G2Scraper(),
    "capterra": CapterraScraper(),
    "trustradius": TrustRadiusScraper(),
    "hackernews": HackerNewsScraper()  # ✅ live demo source
     }

    def run(self, company, source, start_date, end_date):
        scraper = self.SOURCES[source]
        product_id = scraper.get_product_id(company)

        with ThreadPoolExecutor(max_workers=3) as executor:
            future = executor.submit(
                scraper.scrape,
                product_id,
                start_date,
                end_date
            )
            return future.result()
