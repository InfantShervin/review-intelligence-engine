import argparse
from datetime import datetime
from core.manager import ScraperManager
from core.exporter import export
from core.validator import validate_dates
from core.metrics import Metrics
from utils.logger import setup_logger

setup_logger()

parser = argparse.ArgumentParser(description="Review Intelligence Engine")
parser.add_argument("--company", required=True)
parser.add_argument("--source", required=True, choices=["g2", "capterra", "trustradius"])
parser.add_argument("--start_date", required=True)
parser.add_argument("--end_date", required=True)
parser.add_argument("--output", default="output/reviews.json")

args = parser.parse_args()

start = datetime.fromisoformat(args.start_date)
end = datetime.fromisoformat(args.end_date)
validate_dates(start, end)

metrics = Metrics()

manager = ScraperManager()
reviews = manager.run(args.company, args.source, start, end)

metrics.reviews_collected = len(reviews)

export(reviews, args.output)

print("✔ Scraping completed")
print("📊 Metrics:", metrics.summary())
