import httpx
from selectolax.parser import HTMLParser
from database import SessionLocal, HistoricalData, create_tables
from logs_config import logger

def clear_value_to_float(text: str) -> float:
    try:
        clean = text.strip().replace(',', '.')
        return float(clean)
    except ValueError:
        return 0.0

def execute_scraper():
    url = "https://www.bcv.org.ve/"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    try:
        with httpx.Client(headers=headers, verify=False, timeout=30.0) as client:
            logger.info("Iniciando conexión con el BCV...")
            response = client.get(url)
            response.raise_for_status()
        tree = HTMLParser(response.text)
        node = tree.css_first("#dolar strong")

        if(node):
            value_raw = node.text().strip()

            clean_value = clear_value_to_float(value_raw)

            if clean_value > 0:
                db = SessionLocal()

                new_reg = HistoricalData(value=float(clean_value))

                db.add(new_reg)
                db.commit()
                db.close()

                logger.info(f"Value: $ {clean_value} registered on Postgres")
            else:
                logger.warning("Value received not valid")
        else:
            logger.error("Selector not founded.")
    except httpx.HTTPStatusError as e:
        logger.error(f"Server response error: {e}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    create_tables()
    execute_scraper()