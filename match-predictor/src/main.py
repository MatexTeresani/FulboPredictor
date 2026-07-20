from src.utils.logger import setup_logger, get_logger
from src.pipelines.data_pipeline import run_data_pipeline


logger = get_logger(__name__)


def main():
    setup_logger()

    logger.info("Starting application.")

    run_data_pipeline()

    logger.info("Application finished.")


if __name__ == "__main__":
    main()