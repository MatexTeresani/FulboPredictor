import logging
import sys
from pathlib import Path
from typing import Optional
from logging.handlers import RotatingFileHandler

_LOGGER_CONFIGURED = False


def setup_logger(level: int = logging.INFO) -> None:
    """
    Configure the root logger only once.
    """

    global _LOGGER_CONFIGURED

    if _LOGGER_CONFIGURED:
        return

    # Project root
    root_dir = Path(__file__).resolve().parents[2]

    # logs/
    logs_dir = root_dir / "logs"
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "app.log"

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # File
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers.clear()

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    _LOGGER_CONFIGURED = True


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Returns a configured logger.
    """

    if not _LOGGER_CONFIGURED:
        setup_logger()

    return logging.getLogger(name)
"""
Cómo usarlo

En cualquier archivo:

from src.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Downloading Premier League dataset...")

o

logger.debug("Loaded dataframe with %d rows", len(df))

o

logger.warning("Missing values detected.")

o

logger.error("Dataset could not be loaded.")


Para excepciones:

try:
    ...
except Exception:
    logger.exception("Unexpected error while training the model.")


Nota:
setup_logger() debe llamarse una sola vez al iniciar la aplicación
(por ejemplo en src/main.py o en el pipeline principal). No es necesario
llamarlo en cada archivo.
"""