import csv
import os
import logging
import sys

logger = logging.getLogger(__name__)



def load_input_titles(input_path):
    try:
        with open(input_path, "r", encoding="utf-8") as input_books:
            csvreader = csv.DictReader(input_books)
            data = list(csvreader)
            logger.info(f"Loaded {len(data)} rows from CSV")
            return data
        
    except FileNotFoundError:
        logger.error("File doesn't exist")
        sys.exit(1)
    

def save_data(processed_entries, output_path):

    if not processed_entries:
        logger.info("No data to save, exiting...")
        sys.exit(1)
    try:
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok = True)
        with open(output_path, "w", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "price", "rating", "available", "user_name", "email", "company"],
                lineterminator="\n"
            )

            writer.writeheader()

            for row in processed_entries:
                writer.writerow(row)
                
        logger.info(f"Data written to {output_path} successfully")

    except IOError:
        logger.error("Failed to write file")


