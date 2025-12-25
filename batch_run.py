from datetime import datetime
from core.manager import ScraperManager
from core.exporter import export

# 🔹 Companies / keywords to try
COMPANIES = [
    "notion",
    "slack",
    "jira",
    "asana",
    "figma"
]

# 🔹 Sources to try (Hacker News added for live scraping)
SOURCES = [
    "hackernews",   # ✅ live, unblocked
    "trustradius",  # SaaS reviews (may be blocked)
    "g2",
    "capterra"
]

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2025, 12, 31)

OUTPUT_FILE = "output/batch_reviews.json"


def run_batch():
    manager = ScraperManager()
    all_reviews = []

    for company in COMPANIES:
        for source in SOURCES:
            print(f"\n🔍 Trying {source.upper()} for {company}...")

            try:
                reviews = manager.run(
                    company=company,
                    source=source,
                    start_date=START_DATE,
                    end_date=END_DATE
                )

                if reviews:
                    print(f"✅ Collected {len(reviews)} reviews")
                    all_reviews.extend(reviews)
                else:
                    print("⚠️ No reviews found or blocked")

            except Exception as e:
                print("❌ Blocked or inaccessible, skipping")

    export(all_reviews, OUTPUT_FILE)

    print("\n📦 Batch run completed")
    print(f"📊 Total reviews collected: {len(all_reviews)}")
    print(f"📁 Output written to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_batch()

