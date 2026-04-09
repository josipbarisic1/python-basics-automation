import argparse
import os
import logging

from writer import load_input_titles
from scraper import scrape_data
from api import fetch_data
from processor import process_data
from processor import filter_books
from enricher import enrich_data
from writer import save_data
from config import load_config

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Path to input file")
parser.add_argument("--output", help = "Path to output file")
args = parser.parse_args()

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

if __name__ == "__main__":
    main()