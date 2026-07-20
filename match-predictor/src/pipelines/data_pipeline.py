from src.data.loader import (
    list_raw_datasets,
    load_csv,
    save_processed_dataset,
)

from src.data.normalize import normalize_schema
from src.data.dataset_identity import identify_dataset
from src.data.preprocessing import preprocess

from src.utils.logger import get_logger


logger = get_logger(__name__)


def run_data_pipeline() -> None:
    """
    Execute the complete data preparation pipeline.

    Flow:
        Raw CSV
            ↓
        Load
            ↓
        Normalize schema
            ↓
        Identify dataset
            ↓
        Preprocess
            ↓
        Save processed data
    """

    logger.info("Starting data pipeline.")

    for path in list_raw_datasets():

        logger.info("Processing dataset: %s", path.name)

        # Load raw CSV
        df = load_csv(path)

        # Convert external schemas into canonical schema
        df = normalize_schema(df)

        # Extract dataset metadata
        identity = identify_dataset(df)

        logger.info(
            "Dataset identity | Competition: %s | Season: %s",
            identity.competition,
            identity.season,
        )

        # Clean and prepare data
        df = preprocess(df)

        # Save processed dataset
        save_processed_dataset(
            df,
            path.name,
        )

    logger.info("Data pipeline finished.")


if __name__ == "__main__":
    run_data_pipeline()