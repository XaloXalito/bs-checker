import os
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    
    log_dir = "log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("scraper_bcv")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        log_file = os.path.join(log_dir, "scraper.log")
        file_handler = TimedRotatingFileHandler(
            log_file, when="midnight", interval=1, backupCount=30, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        file_handler.suffix = "%Y-%m-%d"

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()