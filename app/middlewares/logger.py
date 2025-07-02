
import logging
import os
from core.config import settings

LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s"
LOG_FILE = "logs/app.log"

def setup_logger():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    logger = logging.getLogger("social-media-app")
    logger.setLevel(settings.LOG_LEVEL)

    # Avoid adding handlers multiple times in dev
    if not logger.hasHandlers():
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(settings.LOG_LEVEL)
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(console_handler)

        # File handler
        file_handler = logging.FileHandler(LOG_FILE, mode="a")
        file_handler.setLevel(settings.LOG_LEVEL)
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(file_handler)

    return logger