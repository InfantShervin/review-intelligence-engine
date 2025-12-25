from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Review(BaseModel):
    source: str
    company: str
    title: Optional[str]
    review: str
    date: datetime
    rating: Optional[float]
    reviewer: Optional[str]
    url: Optional[str]
