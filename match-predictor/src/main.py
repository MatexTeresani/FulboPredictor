from src.utils.logger import setup_logger, get_logger
from src.config.settings import RAW_DATA_DIR


def download_data():
    logger = get_logger("downloader")
    logger.info("Starting data download...")
    logger.info("Using RAW data directory: %s", RAW_DATA_DIR)


def main():
    setup_logger()
    download_data()


if __name__ == "__main__":
    main()