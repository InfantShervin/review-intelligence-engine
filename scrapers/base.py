from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    def get_product_id(self, company: str) -> str:
        pass

    @abstractmethod
    def scrape(self, product_id, start_date, end_date):
        pass
