import logging
import pandas as pd
from extractor import DataExtractor
from config import file_paths

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline(file_path):
    logger.info("Data extraction pipeline started")
    try:
        extractor = DataExtractor(file_path)
        df = extractor.extract()
        print(df.head())
        logger.info("Data extraction pipeline completed successfully")
    except ValueError as ve:
        logger.warning(f"Skipping file due to validation/extraction error: {file_path} | {ve}")

    except Exception as e:
        logger.error(f"Critical failure: {file_path} | {e}")


if __name__ == "__main__":    
    for file in file_paths:
        run_pipeline(file)