import logging
from pathlib import Path 

logger = logging.getLogger(__name__)

def input_scan_files(settings):
    '''
    scan input files and read files names based on supported extension
    '''
    if not settings:
        logger.error("Configuration is empty or invalid")
        return None
    
    input_directory = settings.get("input_directory")
    supported_extension = settings.get("supported_extension")
    supported_extension = supported_extension.lower()

    if not input_directory:
        logger.error("Input directory in configuration is empty or invalid")
        return None
    if not supported_extension:
        logger.error("Supported extension in configuration is empty or invalid")
        return None 
    
    logger.info(f"Scanning directory: {input_directory}")

    input_path = Path(input_directory)
    full_input_path = input_path.resolve()

    if not input_path.exists():
        logger.error(f"Input path does not exist: {full_input_path}")
        return None
    
    if not input_path.is_dir():
        logger.error(f"Path is not a directory: {full_input_path}")
        return None

    file_names = []

    for file in input_path.iterdir():
        if file.is_file() and file.suffix.lower() == supported_extension:
            file_names.append(file.name)

    files = sorted(file_names)
    file_count = len(files)

    if(file_count == 0):
        logger.warning("No input file was found")
        return files
    else:
        logger.info(f"{file_count} supported files found") if file_count > 1 else logger.info (f"{file_count} supported file found")
        for file in files:
            logger.info(f"File detected: {file}")
        return files