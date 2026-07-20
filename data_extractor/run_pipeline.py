import logging
import pandas as pd
from extractor import DataExtractor
from validators import DataValidator
from config import file_paths, VALIDATION_CONFIG

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline(file_path, config):
    logger.info("Pipeline started")
    try:
        extractor = DataExtractor(file_path)
        df = extractor.extract()
        
        validator = DataValidator(df)
        validator.run_all_validations(config)

        logger.info("Pipeline completed successfully")

    except ValueError as ve:
        logger.warning(f"Skipping file due to validation/extraction error: {file_path} | {ve}")

    except Exception as e:
        logger.error(f"Critical failure: {file_path} | {e}")


if __name__ == "__main__":    
    for file in file_paths:
        run_pipeline(file, VALIDATION_CONFIG)

