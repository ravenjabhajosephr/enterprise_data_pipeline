import logging
from app.config import load_settings
from app.file_handler import input_scan_files
from app.logger import setup_logger

logger = logging.getLogger(__name__)

def main():
    try:
        settings = load_settings()
    except Exception as e:
        print(f"Critical error (Config file not found): {e}")
        return
    
    setup_logger(settings)
    logger.info("Pipeline started")

    try:
        files = input_scan_files(settings)
        if files is None:
            logger.error("File Scan failed")
            return 
    except Exception as e:
        logger.error(f"Error while scanning input files: {e}")

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()