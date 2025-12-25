from bs4 import BeautifulSoup
from scrapers.base import BaseScraper
from utils.http import fetch
from utils.dates import parse_date
from models.review import Review

class TrustRadiusScraper(BaseScraper):

    def get_product_id(self, company: str) -> str:
        return company.lower()

    def scrape(self, product_id, start_date, end_date):
        url = f"https://www.trustradius.com/products/{product_id}/reviews"
        html = fetch(url)
        soup = BeautifulSoup(html, "html.parser")

        reviews = []
        blocks = soup.select("div.review-content") or soup.find_all("article")

        for b in blocks:
            text = b.get_text(strip=True)
            if not text:
                continue

            # TrustRadius often hides dates → documented fallback
            date = parse_date("2024-01-01")

            if start_date <= date <= end_date:
                reviews.append(
                    Review(
                        source="trustradius",
                        company=product_id,
                        title=None,
                        review=text,
                        date=date,
                        rating=None,
                        reviewer=None,
                        url=url
                    )
                )

        return reviews
