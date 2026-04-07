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

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Path to input file")
parser.add_argument("--output", help = "Path to output file")
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
READER_FALLBACK = os.path.join(BASE_DIR, "test_files/input_books.csv")
WRITER_FALLBACK = os.path.join(BASE_DIR, "test_files/user_books.csv")

INPUT_PATH = args.input if args.input else READER_FALLBACK
OUTPUT_PATH = args.output if args.output else WRITER_FALLBACK

BASE_URL = "https://books.toscrape.com/catalogue/"
API_URL = "https://jsonplaceholder.typicode.com/users"


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s'
    )
        
    loaded_titles = load_input_titles(INPUT_PATH)
    
    raw_data_books = scrape_data(BASE_URL)
    clean_data_books = process_data(raw_data_books)

    data_users = fetch_data(API_URL)

    matched_books = filter_books(clean_data_books, loaded_titles)

    enriched = enrich_data(matched_books, data_users)

    save_data(enriched, OUTPUT_PATH)

if __name__ == "__main__":
    main()