from app.config import load_settings
from app.file_handler import input_scan_files
from app.logger import setup_logger

def main():
    logger = setup_logger()

    logger.info("Pipeline started")

    try:
        settings = load_settings()
        logger.info("Settings loaded")
    except Exception as e:
        logger.error("Setting configuration is missing: ", e)
        return

    try:
        files = input_scan_files(settings)

        if files is None:
            logger.error("The input directory does not exists or invalid")
            return 

        if(len(files) == 0):
            logger.warning("No input file was found")
        else:
            file_count = len(files)
            logger.info(f"{file_count} supported files found")
            for file in files:
                logger.info(f"File detected: {file}") 
    except Exception as e:
        logger.error("Error while scanning input files", e)

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()