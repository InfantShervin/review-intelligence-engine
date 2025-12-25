import requests
from datetime import datetime
from scrapers.base import BaseScraper
from models.review import Review


class HackerNewsScraper(BaseScraper):
    """
    Live public scraper using Hacker News Algolia API.
    This source is used to demonstrate successful live scraping
    without access restrictions.
    """

    def get_product_id(self, company: str) -> str:
        # Use company name as search keyword
        return company.lower()

    def scrape(self, product_id, start_date, end_date):
        reviews = []

        # ✅ Query BOTH stories and comments (important fix)
        url = (
            "https://hn.algolia.com/api/v1/search?"
            f"query={product_id}&tags=story,comment"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        for hit in data.get("hits", []):
            # Text can come from story title or comment text
            text = hit.get("comment_text") or hit.get("title")
            created_at = hit.get("created_at")

            if not text or not created_at:
                continue

            try:
                # Proper ISO date parsing
                date = datetime.fromisoformat(created_at.replace("Z", ""))
            except Exception:
                continue

            # Date range filtering
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
