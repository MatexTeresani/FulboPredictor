from dataclasses import dataclass
from datetime import datetime

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class DatasetIdentity:
    """
    Metadata that identifies a football dataset.
    """

    competition: str | None
    season: str | None

    start_date: datetime | None
    end_date: datetime | None

    matches: int
    features: int


def identify_dataset(df: pd.DataFrame) -> DatasetIdentity:
    """
    Extract dataset identity from normalized dataframe.
    """

    logger.info("Identifying dataset...")

    identity = DatasetIdentity(
        competition=_extract_competition(df),
        season=_extract_season(df),
        start_date=_extract_date_range(df)[0],
        end_date=_extract_date_range(df)[1],
        matches=len(df),
        features=len(df.columns),
    )

    logger.info(
        "Dataset identity: %s | %s | %s matches",
        identity.competition,
        identity.season,
        identity.matches,
    )

    return identity


def _extract_competition(df: pd.DataFrame) -> str | None:
    """
    Extract competition identifier.
    """

    if "competition" not in df.columns:
        logger.warning("Competition column not found.")
        return None

    values = df["competition"].dropna().unique()

    if len(values) == 0:
        return None

    if len(values) > 1:
        logger.warning(
            "Multiple competitions detected: %s",
            values,
        )

    return str(values[0])


def _extract_date_range(
    df: pd.DataFrame,
) -> tuple[datetime | None, datetime | None]:
    """
    Extract match date range.
    """

    if "match_date" not in df.columns:
        logger.warning("Match date column not found.")
        return None, None

    dates = pd.to_datetime(
        df["match_date"],
        dayfirst=True,
        errors="coerce",
    ).dropna()

    if dates.empty:
        return None, None

    return dates.min(), dates.max()


def _extract_season(
    df: pd.DataFrame,
) -> str | None:
    """
    Infer season from dates.
    """

    start_date, end_date = _extract_date_range(df)

    if start_date is None or end_date is None:
        return None

    if start_date.year == end_date.year:
        return str(start_date.year)

    return f"{start_date.year}-{end_date.year}"