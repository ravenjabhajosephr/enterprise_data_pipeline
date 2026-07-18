import os
import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def _get_file_size(self):
        return Path(self.file_path).stat().st_size

    def _read_csv(self):
        logger.info(f"Reading csv file...")
        try:
            if self._get_file_size() == 0:
                raise ValueError(f"File is empty: {self.file_path}")

            df =  pd.read_csv(self.file_path)
            df_len = len(df)
            logger.info("CSV file data extraction completed")
            logger.info(f"Total {'records' if df_len > 1 else 'record'} extracted: {df_len}")
            return df
        except Exception as e:
            raise RuntimeError(f"Error in reading CSV file: {self.file_path} | {e}")
        
    def _read_excel(self):
        logger.info("Reading excel file...")
        try:
            if self._get_file_size() == 0:
                raise ValueError(f"File is empty: {self.file_path}")
                    
            df = pd.read_excel(io=self.file_path, engine="openpyxl")
            df_len = len(df)
            logger.info("Excel file data extraction completed")
            logger.info(f"Total {'records' if df_len > 1 else 'record'} extracted: {df_len}")
            return df
        except Exception as e:
            raise RuntimeError(f"Error in reading excel file: {self.file_path} | {e}")
        
    def _read_json(self):
        logger.info("Reading json file...")
        try:
            if self._get_file_size() == 0:
                raise ValueError(f"File is empty: {self.file_path}")
                
            df = pd.read_json(self.file_path)
            df_len = len(df)
            logger.info("JSON file data extraction completed")
            logger.info(f"Total {'records' if df_len > 1 else 'record'} extracted: {df_len}")
            return df
        except Exception as e:
            raise RuntimeError(f"Error in reading JSON file: {self.file_path} | {e}")
    
    def _read_txt(self):
        logger.info("Reading txt file...")
        try:
            if self._get_file_size() == 0:
                raise ValueError(f"File is empty: {self.file_path}")
                
            try: 
                df = pd.read_csv(self.file_path)
                df_len = len(df)
                logger.info("TXT file parsed as structured delimited text")
                logger.info(f"Total {'records' if df_len > 1 else 'record'} extracted: {df_len}")
                return df
            except Exception as e:
                logger.info(f"TXT file: {self.file_path} parsed as structured delimited text failed. Reading as raw logs. Exception: {e}")

                with open(self.file_path, "r", encoding="utf-8") as file:
                    parsed_lines = [line.strip() for line in file if line.strip()]
                df = pd.DataFrame({"raw_logs" : parsed_lines})
                df_len = len(df)
                logger.info("TXT file data extraction completed")
                logger.info(f"Total {'records' if df_len > 1 else 'record'} extracted: {df_len}")
                return df
        except Exception as e:
            raise RuntimeError(f"Error in reading text file: {self.file_path} | {e}")
    
    def extract(self):
        extension = os.path.splitext(self.file_path)[1].lower()

        logger.info("Data extraction initiated")

        if extension == ".csv":
            return self._read_csv()
        elif extension in [".xlsx", ".xls"]:
            return self._read_excel()
        elif extension == ".json":
            return self._read_json()
        elif extension in [".txt", ".log"]:
            return self._read_txt()
        else:
            raise ValueError("Unsupported format")
        