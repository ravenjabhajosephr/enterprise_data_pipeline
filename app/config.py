# import libraries
import json
import logging
from pathlib import Path 

def load_settings():
    '''
    load settings from config file
    '''
    print("Loading configuration started")
    config_path = Path("config/settings.json")

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    else:
        with config_path.open("r", encoding="utf-8") as file:
            settings = json.load(file)
            print("Configuration loaded successfully")
            return settings

