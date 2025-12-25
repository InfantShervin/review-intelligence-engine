import time

class Metrics:
    def __init__(self):
        self.start_time = time.time()
        self.pages_scraped = 0
        self.reviews_collected = 0

    def summary(self):
        return {
            "pages_scraped": self.pages_scraped,
            "reviews_collected": self.reviews_collected,
            "execution_time_seconds": round(time.time() - self.start_time, 2)
        }
