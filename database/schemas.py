from pydantic import BaseModel,ConfigDict
from datetime import datetime
from typing import List, Optional

class HistoricalDataBase(BaseModel):
    value: float
    date: datetime

    model_config = ConfigDict(from_attributes=True)

class SourceBase(BaseModel):
    id: int
    name: str
    currency: str
    url: str

    model_config = ConfigDict(from_attributes=True)

class SourceWithData(SourceBase):
    historical_data: List[HistoricalDataBase] = []