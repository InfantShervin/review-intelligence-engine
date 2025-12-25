from bs4 import BeautifulSoup
from scrapers.base import BaseScraper
from utils.http import fetch
from utils.dates import parse_date
from models.review import Review


class G2Scraper(BaseScraper):

    def get_product_id(self, company: str) -> str:
        return company.lower()

    def scrape(self, product_id, start_date, end_date):
        reviews = []
        page = 1

        while True:
            url = f"https://www.g2.com/products/{product_id}/reviews?page={page}"
            html = fetch(url)
            soup = BeautifulSoup(html, "html.parser")

            containers = soup.select("div.paper")
            if not containers:
                break

            for c in containers:
                body_tag = c.select_one("[itemprop='reviewBody']") or c.find("p")
                date_tag = c.find("time")

                if not body_tag or not date_tag:
                    continue

                try:
                    date = parse_date(date_tag.get("datetime") or date_tag.text)
                except Exception:
                    continue

                if start_date <= date <= end_date:
                    reviews.append(
                        Review(
                            source="g2",
                            company=product_id,
                            title=None,
                            review=body_tag.get_text(strip=True),
                            date=date,
                            rating=None,
                            reviewer=None,
                            url=url
                        )
                    )

            page += 1

        return reviews
