from bs4 import BeautifulSoup
from scrapers.base import BaseScraper
from utils.http import fetch
from utils.dates import parse_date
from models.review import Review


class CapterraScraper(BaseScraper):

    def get_product_id(self, company: str) -> str:
        return company.lower()

    def scrape(self, product_id, start_date, end_date):
        url = f"https://www.capterra.com/p/{product_id}/reviews/"
        html = fetch(url)
        soup = BeautifulSoup(html, "html.parser")

        reviews = []
        containers = soup.select("div.review")

        for c in containers:
            text_tag = c.find("p")
            date_tag = c.find("time")

            if not text_tag or not date_tag:
                continue

            try:
                date = parse_date(date_tag.get("datetime") or date_tag.text)
            except Exception:
                continue

            if start_date <= date <= end_date:
                reviews.append(
                    Review(
                        source="capterra",
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
