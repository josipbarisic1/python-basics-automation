import argparse
import os
import logging
import sys

from writer import load_input_titles
from scraper import scrape_data
from api import fetch_data
from processor import process_data
from processor import filter_books
from enricher import enrich_data
from writer import save_data
from config import load_config

parser = argparse.ArgumentParser(
    description="Full data pipeline: scrapes books, filters by input CSV, enriches with API data"
)
parser.add_argument(
    "--input",
    help="Path to input CSV file (default: from config.json)",
    metavar="FILE"
)
parser.add_argument(
    "--output",
    help="Path to output CSV file (default: from config.json)",
    metavar="FILE"
)
args = parser.parse_args()

if args.input and not os.path.exists(args.input):
    print(f"[ERROR] Input file not found: {args.input}")
    sys.exit(1)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s'
    )
    config = load_config()

    input_path = args.input if args.input else config["paths"]["input"]
    output_path = args.output if args.output else config["paths"]["output"]
        
    loaded_titles = load_input_titles(input_path)
    raw_data_books = scrape_data(config["scraper"])
    clean_data_books = process_data(raw_data_books, config["processor"])
    data_users = fetch_data(config["api"])
    matched_books = filter_books(clean_data_books, loaded_titles)
    enriched = enrich_data(matched_books, data_users)
    save_data(enriched, output_path)
    
    print(f"\n[SUCCESS] Pipeline completed successfully")
    print(f"  Books matched: {len(enriched)}")
    print(f"  Output: {output_path}")

if __name__ == "__main__":
    main()