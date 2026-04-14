import gspread
import json
import os
import logging
import sys

logger = logging.getLogger(__name__)

def load_config(config_path=None):
    if config_path is None:
        base_dir = os.path.dirname(__file__)
        config_path = os.path.join(base_dir, "config.json")
    
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        logger.info(f"Loaded config from {config_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config: {e}")
        sys.exit(1)

def connect_to_sheet(config):
    service_account_path = os.path.join(
        os.path.dirname(__file__), 
        config['service_account_file']
    )
    
    gc = gspread.service_account(filename=service_account_path)
    sheet = gc.open_by_key(config['sheet_id'])
    return sheet.sheet1

def read_data(worksheet):
    data = worksheet.get_all_records()
    return data

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s'
    )
    
    config = load_config()
    worksheet = connect_to_sheet(config)
    data = read_data(worksheet)
    
    logger.info(f"[INFO] Read {len(data)} rows from Google Sheets")
    for row in data[:3]:
        print(row)

if __name__ == "__main__":
    main()
