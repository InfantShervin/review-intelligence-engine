import requests
from datetime import datetime
from scrapers.base import BaseScraper
from models.review import Review

class HackerNewsScraper(BaseScraper):
    """
    Live public source using Hacker News (Algolia API).
    Used to demonstrate live scraping without blocking.
    """

    def get_product_id(self, company: str) -> str:
        return company.lower()

    def scrape(self, product_id, start_date, end_date):
        url = (
            "https://hn.algolia.com/api/v1/search?"
            f"query={product_id}&tags=comment"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        reviews = []

        for hit in data.get("hits", []):
            text = hit.get("comment_text")
            created_at = hit.get("created_at")

            if not text or not created_at:
                continue

            date = datetime.fromisoformat(created_at.replace("Z", ""))

            if start_date <= date <= end_date:
                reviews.append(
                    Review(
                        source="hackernews",
                        company=product_id,
                        title=None,
                        review=text,
                        date=date,
                        rating=None,
                        reviewer=hit.get("author"),
                        url=hit.get("url")
                    )
                )

        return reviews
