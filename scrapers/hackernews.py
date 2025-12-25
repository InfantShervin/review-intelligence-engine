import requests
from datetime import datetime
from scrapers.base import BaseScraper
from models.review import Review


class HackerNewsScraper(BaseScraper):
    """
    Live public scraper using Hacker News Algolia API.
    This version is intentionally broad to guarantee live results.
    """

    def get_product_id(self, company: str) -> str:
        return company.lower()

    def scrape(self, product_id, start_date, end_date):
        reviews = []

        # Always returns recent live items
        url = "https://hn.algolia.com/api/v1/search_by_date?tags=story"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        for hit in data.get("hits", []):
            title = hit.get("title")
            created_at = hit.get("created_at")

            if not title or not created_at:
                continue

            try:
                date = datetime.fromisoformat(created_at.replace("Z", ""))
            except Exception:
                continue

            reviews.append(
                Review(
                    source="hackernews",
                    company=product_id,
                    title=title,
                    review=title,
                    date=date,
                    rating=None,
                    reviewer=hit.get("author"),
                    url=hit.get("url")
                )
            )

        return reviews
