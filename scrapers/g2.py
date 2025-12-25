from bs4 import BeautifulSoup
from scrapers.base import BaseScraper
from utils.http import fetch
from scrapers.selenium_fallback import fetch_with_selenium
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

            # 🔴 If requests is blocked → Selenium fallback
            if html is None:
                soup = fetch_with_selenium(url)
            else:
                soup = BeautifulSoup(html, "html.parser")

            blocks = soup.select("div.paper") or soup.find_all("article")
            if not blocks:
                break

            for b in blocks:
                body = b.select_one("[itemprop='reviewBody']") or b.find("p")
                date_tag = b.find("time")

                if not body or not date_tag:
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
                            review=body.get_text(strip=True),
                            date=date,
                            rating=None,
                            reviewer=None,
                            url=url
                        )
                    )

            page += 1

        return reviews
