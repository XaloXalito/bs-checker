#DATABASE
from database.connection import SessionLocal
from database.models.historical import HistoricalData
from database.models.source import Source

#SCRAPERS
from scrapers.bcv import BCVScrapper

#LOGS
from logs_config import logger

SCRAPERS_LIST = {
    "BCV": BCVScrapper(selector="#dolar strong"),
    "BCV_EURO": BCVScrapper(selector="#euro strong"),
}

def execute():
    db = SessionLocal()
    
    try:
        active_sources = db.query(Source).all()

        for source in active_sources:
            if source.name in SCRAPERS_LIST:
                logger.info(f"INITIALIZING: {source.name} ({source.currency})")
                try:
                    scraper = SCRAPERS_LIST[source.name]
                    price = scraper.extract()

                    new_reg = HistoricalData(value=price, source_id=source.id)
                    db.add(new_reg)
                    logger.info(f"SUCCESS: {source.name} => {price}")
                except Exception as e:
                    logger.error(f"Error processing {source.name}: {e}")
    
        db.commit()
    except Exception as e:
        logger.error(f"Critical Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    execute()