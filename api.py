from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.connection import SessionLocal
from database.models import Source, HistoricalData
from database import schemas

app = FastAPI(title="Scraper API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message":"API is running"}

@app.get("/sources", response_model=List[schemas.SourceBase])
def get_sources(db: Session = Depends(get_db)):
    return db.query(Source).all()

@app.get("/latest", response_model=List[schemas.SourceWithData])
def get_latest_prices(db: Session = Depends(get_db)):
    return db.query(Source).all()


@app.get("/history/{source_name}", response_model=schemas.SourceWithData)
def get_source_history(source_name: str, db: Session = Depends(get_db)):
    source = db.query(Source).filter(Source.name == source_name.upper()).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source