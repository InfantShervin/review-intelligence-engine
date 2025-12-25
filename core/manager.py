from scrapers.g2 import G2Scraper
from scrapers.capterra import CapterraScraper
from scrapers.trustradius import TrustRadiusScraper


class ScraperManager:

    SOURCES = {
        "g2": G2Scraper(),
        "capterra": CapterraScraper(),
        "trustradius": TrustRadiusScraper()
    }

    def run(self, company, source, start_date, end_date):
        scraper = self.SOURCES[source]
        product_id = scraper.get_product_id(company)
        return scraper.scrape(product_id, start_date, end_date)
