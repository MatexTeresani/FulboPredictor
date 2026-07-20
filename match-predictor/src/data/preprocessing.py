import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicated matches.
    """

    before = len(df)

    df = df.drop_duplicates()

    logger.info(
        "Removed %d duplicated rows.",
        before - len(df),
    )

    return df


def drop_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove completely empty rows.
    """

    before = len(df)

    df = df.dropna(how="all")

    logger.info(
        "Removed %d empty rows.",
        before - len(df),
    )

    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply basic data cleaning.
    """

    logger.info("Starting preprocessing.")

    df = remove_duplicates(df)
    df = drop_empty_rows(df)

    logger.info(
        "Preprocessing finished."
    )

    return df