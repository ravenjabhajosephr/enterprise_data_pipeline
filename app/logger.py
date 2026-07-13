import logging
from pathlib import Path

def setup_logger(settings):
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "pipeline.log"

    log_level_str = settings.get("log_level", "INFO")

    log_level = getattr(logging, log_level_str.upper(), logging.INFO)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    return logging
