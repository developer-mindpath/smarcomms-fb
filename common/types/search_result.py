from pydantic import BaseModel
from typing import Optional


class SearchResult(BaseModel):
    answer: Optional[str]
    similarity: float = 0.0
