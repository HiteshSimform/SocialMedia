import logging
import os
from logging.handlers import RotatingFileHandler
from core.config import settings

# Constants
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s"
LOG_FILE = "logs/app.log"
MAX_LOG_FILE_SIZE = 10 * 1024 * 1024  # 10 MB max per log file
BACKUP_COUNT = 5  # Keep 5 backup logs


def setup_logger():
    """
    Setup logger with both file and console handlers. Includes log rotation.
    """
    # Ensure logs directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # Create logger instance
    logger = logging.getLogger("social-media-app")

    # Set log level based on the environment
    logger.setLevel(
        settings.LOG_LEVEL
    )  # Set global log level (e.g., DEBUG, INFO, etc.)

    # Avoid adding handlers multiple times in development
    if not logger.hasHandlers():
        # Console handler for development or local environments
        console_handler = logging.StreamHandler()
        console_handler.setLevel(settings.LOG_LEVEL)  # Console log level
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        # File handler with rotation for production environments
        file_handler = RotatingFileHandler(
            LOG_FILE, maxBytes=MAX_LOG_FILE_SIZE, backupCount=BACKUP_COUNT, mode="a"
        )
        file_handler.setLevel(settings.LOG_LEVEL)  # File log level
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        # Add handlers to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
