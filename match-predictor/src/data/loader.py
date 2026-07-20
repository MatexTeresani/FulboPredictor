from pathlib import Path

import pandas as pd

from src.config.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV file.
    """

    logger.info(f"Loading dataset: {path}")

    return pd.read_csv(path)


def load_raw_dataset(filename: str) -> pd.DataFrame:
    """
    Load a dataset from data/raw.
    """

    return load_csv(RAW_DATA_DIR / filename)


def save_processed_dataset(df: pd.DataFrame, filename: str) -> None:
    """
    Save a processed dataset.
    """

    output = PROCESSED_DATA_DIR / filename

    logger.info(f"Saving dataset: {output}")

    df.to_csv(output, index=False)


def list_raw_datasets() -> list[Path]:
    """
    Return every CSV inside raw.
    """

    return sorted(RAW_DATA_DIR.glob("*.csv"))