import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataValidator:
    def __init__(self, df):
        self.df = df
    
    def _validate_columns(self, expected_columns):
        logger.info(f"Validating required columns")

        missing_cols = [col for col in expected_columns if col not in self.df.columns]

        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        logger.info(f"Column validation passed")
        return True
    
    def _check_nulls(self, no_null_columns):
        logger.info(f"Checking null values for the required columns")
        missing_cols = []
        null_cols = {}
        for col in no_null_columns:
            if col not in self.df.columns:
                missing_cols.append(col)
            else:
                if self.df[col].isnull().any():
                    null_count = self.df[col].isnull().sum()
                    null_cols[col] = null_count
        
        if missing_cols and null_cols:
            error_message = ""
            if missing_cols:
                error_message += f"Missing required columns: {missing_cols}"
            if null_cols:
                error_message += f"Columns with null values: {null_cols}"
            raise ValueError(error_message)
        elif missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        elif null_cols:
            raise ValueError(f"Columns with null values: {null_cols}")
        logger.info(f"Null validation passed")
        return True
    
    def _validate_dtypes(self, column_types):
        logger.info(f"Checking column data types for the required columns")
        missing_cols = []
        for col, dtype in column_types.items():
            if col not in self.df.columns:
                missing_cols.append(col)
            else:
                actual_type = str(self.df[col].dtype)
                if actual_type != dtype:
                    raise ValueError(f"Column '{col}' has incorrect data type. Expected: {dtype}, Actual: {actual_type}")
        
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        logger.info(f"Data type validation passed")
        return True
    
    def _check_duplicates(self, columns):
        logger.info("Checking duplicates")

        for column in columns:
            if column not in self.df.columns:
                raise ValueError(f"Column not found for duplicate check: {column}")

            if self.df[column].duplicated().any():
                dup_count = self.df[column].duplicated().sum()
                raise ValueError(f"Duplicate values found in column: {column}, count: {dup_count}")

        logger.info("Duplicate validation passed")
        return True
    
    def run_all_validations(self, config):
        if not config:
            raise ValueError("Validation configuration is missing")

        expected_columns = config.get("columns", [])
        no_null_columns = config.get("no_nulls", [])
        column_types = config.get("dtypes", {})
        duplicate_columns = config.get("no_duplicates", [])

        logger.info("Validation layer initiated")

        if expected_columns:
            self._validate_columns(expected_columns)
        if no_null_columns:
            self._check_nulls(no_null_columns)
        if column_types:
            self._validate_dtypes(column_types)
        if duplicate_columns:
            self._check_duplicates(duplicate_columns)

        logger.info(f"Validation layer completed")
        return True