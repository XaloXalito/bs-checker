from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True)
    name =  Column(String, unique=True)
    currency = Column(String)
    url = Column(String)

    historical_data = relationship("HistoricalData", back_populates="source")