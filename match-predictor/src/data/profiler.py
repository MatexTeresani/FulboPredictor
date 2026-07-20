import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def profile_dataset(df: pd.DataFrame, name: str = "Dataset") -> None:
    """
    Print useful information about a dataset.
    """

    logger.info("=" * 60)
    logger.info("PROFILE: %s", name)
    logger.info("=" * 60)

    logger.info("Rows: %d", len(df))
    logger.info("Columns: %d", len(df.columns))

    memory = df.memory_usage(deep=True).sum() / (1024 ** 2)
    logger.info("Memory: %.2f MB", memory)

    logger.info("Duplicated rows: %d", df.duplicated().sum())
    logger.info("Empty rows: %d", df.isna().all(axis=1).sum())

    logger.info("")
    logger.info("HEADERS")

    for column in df.columns:
        logger.info(" - %s", column)

    logger.info("")
    logger.info("COLUMN SUMMARY")

    summary = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "nulls": df.isna().sum(),
        "null_%": (df.isna().mean() * 100).round(2),
        "unique": df.nunique(dropna=True),
    })

    print(summary)

    logger.info("")
    logger.info("FIRST 5 ROWS")

    print(df.head())

    logger.info("")
    logger.info("NUMERIC DESCRIPTION")

    print(df.describe(include="number"))