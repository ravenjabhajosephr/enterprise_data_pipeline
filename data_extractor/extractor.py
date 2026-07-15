import os
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        logger.info(f"Reading csv file...")
        try:
            df =  pd.read_csv(self.file_path)
            df_len = len(df)
            logger.info("CSV file data extraction completed")
            logger.info(f"Total {"records" if df_len > 1 else "record"} extracted: {df_len}")
            return df
        except:
            raise RuntimeError(f"Error in reading CSV file: {self.file_path}")
        
    def read_excel(self):
        logger.info("Reading excel file...")
        try:
            df = pd.read_excel(io=self.file_path, engine="openpyxl")
            df_len = len(df)
            logger.info("Excel file data extraction completed")
            logger.info(f"Total {"records" if df_len > 1 else "record"} extracted: {df_len}")
            return df
        except:
            raise RuntimeError(f"Error in reading excel file: {self.file_path}")
        
    def read_json(self):
        logger.info("Reading json file...")
        try:
            df = pd.read_json(self.file_path)
            df_len = len(df)
            logger.info("JSON file data extraction completed")
            logger.info(f"Total {"records" if df_len > 1 else "record"} extracted: {df_len}")
            return df
        except:
            raise RuntimeError(f"Error in reading JSON file: {self.file_path}")
    
    def read_txt(self):
        logger.info("Reading txt file...")
        try:
            parsed_lines = []
            with open(self.file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parsed_lines = line.strip()
                df = pd.DataFrame(parsed_lines, columns=["raw_log"])
                df_len = len(df)
                logger.info("CSV file data extraction completed")
                logger.info(f"Total {"records" if df_len > 1 else "record"} extracted: {df_len}")
        except:
            raise RuntimeError(f"Error in reading text file: {self.file_path}")
    
    def extract(self):
        extension = os.path.splitext(self.file_path)[1].lower()

        logger.info("Data extraction initiated")

        if extension == ".csv":
            return self.read_csv()
            
        elif extension in [".xlsx", ".xls"]:
            df = self.read_excel()
            return df
        elif extension == ".json":
            df = self.read_json()
            return df
        elif extension in [".txt", ".log"]:
            df = self.read_txt()
            return df
        else:
            raise ValueError("Unsupported format")
        