import logging
import pandas as pd
from extractor import DataExtractor
from config import file_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(file_path):
    logger.info("Data extraction pipeline started")
    extractor = DataExtractor(file_path)
    df = extractor.extract()
    # logger.info("")
    # print(df.head())
    logger.info("Data extraction pipeline ended")

if __name__ == "__main__":    
    main(file_path)