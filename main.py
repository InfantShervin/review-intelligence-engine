import argparse
from datetime import datetime
from core.manager import ScraperManager
from core.exporter import export
from utils.logger import setup_logger


setup_logger()

parser = argparse.ArgumentParser(description="Review Intelligence Engine")
parser.add_argument("--company", required=True)
parser.add_argument("--source", required=True, choices=["g2", "capterra"])
parser.add_argument("--start_date", required=True)
parser.add_argument("--end_date", required=True)
parser.add_argument("--output", default="output/reviews.json")

args = parser.parse_args()

start = datetime.fromisoformat(args.start_date)
end = datetime.fromisoformat(args.end_date)

manager = ScraperManager()
reviews = manager.run(args.company, args.source, start, end)

export(reviews, args.output)

print(f"✔ Collected {len(reviews)} reviews")
