import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(log_file="trading_bot.log"):
    """
    Sets up logging to both console and file.
    """
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    # Formatters
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
