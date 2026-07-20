import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


# Canonical column names
COLUMN_MAPPING = {
    # competition
    "Div": "competition",
    "League": "competition",

    # season
    "Season": "season",

    # date
    "Date": "match_date",
    "Time": "match_time",

    # teams
    "HomeTeam": "home_team",
    "Home": "home_team",

    "AwayTeam": "away_team",
    "Away": "away_team",

    # goals
    "FTHG": "home_goals",
    "HG": "home_goals",

    "FTAG": "away_goals",
    "AG": "away_goals",

    # result
    "FTR": "result",
    "Res": "result",
}


def normalize_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize a dataset to the project's canonical schema.

    Unknown columns are preserved.
    """

    logger.info("Normalizing dataset schema...")

    renamed = {}
    ignored = []

    for column in df.columns:
        if column in COLUMN_MAPPING:
            renamed[column] = COLUMN_MAPPING[column]
        else:
            ignored.append(column)

    df = df.rename(columns=renamed)

    logger.info("Renamed %d columns.", len(renamed))

    if ignored:
        logger.info(
            "Keeping %d unmapped columns.",
            len(ignored),
        )

    return df