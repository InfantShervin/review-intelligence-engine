from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Review(BaseModel):
    source: str                 # g2 / capterra / trustradius
    company: str                # company name
    title: Optional[str]        # review title (if available)
    review: str                 # main review text
    date: datetime              # review date
    rating: Optional[float]     # rating if available
    reviewer: Optional[str]     # reviewer name if available
    url: Optional[str]          # source URL
