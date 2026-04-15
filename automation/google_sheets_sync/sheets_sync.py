import gspread
import json
import os
import logging
import sys
import argparse

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="Filters data by Department and creates a new sheet"
)
parser.add_argument(
    "--department",
    help="Department to filter (default: Engineering)",
    metavar="TEXT"
)
args = parser.parse_args()

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

def process_data(data, department):
    filtered = [row for row in data if row['Department'] == department]
    logger.info(f"Filtered to {len(filtered)} rows ({department} only)")
    return filtered

def write_data(worksheet, data, sheet_name="Processed"):
    try:
        spreadsheet = worksheet.spreadsheet
        try:
            target_sheet = spreadsheet.worksheet(sheet_name)
            target_sheet.clear()
        except gspread.exceptions.WorksheetNotFound:
            target_sheet = spreadsheet.add_worksheet(
                title=sheet_name, 
                rows=100, 
                cols=20
            )
        
        if not data:
            logger.warning("No data to write")
            return
        
        headers = list(data[0].keys())
        rows = [headers]
        
        for row in data:
            rows.append([row[key] for key in headers])
        
        target_sheet.update(rows, 'A1')
        logger.info(f"Wrote {len(data)} rows to sheet '{sheet_name}'")
        
    except Exception as e:
        logger.error(f"Failed to write data: {e}")
        sys.exit(1)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s'
    )

    department = args.department if args.department else "Engineering"
    
    config = load_config()
    worksheet = connect_to_sheet(config)
    
    data = read_data(worksheet)
    logger.info(f"Read {len(data)} rows from Google Sheets")
    
    filtered = process_data(data, department)
    
    output_sheet_name = f"{department} Only"
    write_data(worksheet, filtered, output_sheet_name)
    
    print(f"\n[SUCCESS] Processed {len(filtered)} rows")
    print(f"  Department: {department}")
    print(f"  Output sheet: '{output_sheet_name}'")

if __name__ == "__main__":
    main()
