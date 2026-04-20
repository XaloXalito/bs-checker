from database.connection import SessionLocal
from database.models.source import Source
from logs_config import logger

def seed_sources():
    sources_list = [
        {
            "name": "BCV",
            "currency": "USD",
            "url": "https://www.bcv.org.ve/",
        },
        {
            "name": "BCV_EURO",
            "currency": "EUR",
            "url": "https://www.bcv.org.ve/",
        },
    ]

    db = SessionLocal()
    try:
        logger.info("Seeding Database...")
        
        for data in sources_list:
            # Verify if source exist on database
            source_exist = db.query(Source).filter(Source.name == data["name"]).first()
            
            if not source_exist:
                new_source = Source(
                    name=data["name"],
                    currency=data["currency"],
                    url=data["url"]
                )
                db.add(new_source)
                logger.info(f"✅ Source added: {data['name']}")
            else:
                logger.info(f"ℹ️ The source {data['name']} already exist, skipping...")
        
        db.commit()
        logger.info("Seeder success.")
        
    except Exception as e:
        db.rollback()
        logger.error(f"❌ Error while seeding the database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_sources()