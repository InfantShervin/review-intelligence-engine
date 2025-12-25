import requests
from bs4 import BeautifulSoup
from scrapers.base import BaseScraper
from utils.dates import parse_date
from models.review import Review

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

class TrustRadiusScraper(BaseScraper):
    """
    Live TrustRadius scraper using public product pages.
    This works WITHOUT Selenium.
    """

    def get_product_id(self, company: str) -> str:
        return company.lower()

    def scrape(self, product_id, start_date, end_date):
        url = f"https://www.trustradius.com/products/{product_id}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        reviews = []

        # ✅ Correct selector (current TrustRadius)
        blocks = soup.select('section[data-testid="review"]')

        for block in blocks:
            text_tag = block.select_one("p")
            date_tag = block.select_one("time")

            if not text_tag or not date_tag:
                continue

            try:
                date = parse_date(date_tag.get("datetime"))
            except Exception:
                continue

            if start_date <= date <= end_date:
                reviews.append(
                    Review(
                        source="trustradius",
                        company=product_id,
                        title=None,
                        review=text_tag.get_text(strip=True),
                        date=date,
                        rating=None,
                        reviewer=None,
                        url=url
                    )
                )

        return reviews
