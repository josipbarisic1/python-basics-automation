# Book Data Pipeline

**Problem:**  
Need to scrape books, match against target list, enrich with user data - multiple manual steps.

**Solution:**  
Full automated pipeline - scrapes, filters, matches, enriches, exports in one run.

## Structure

Refactored into modules:
- `main.py` -> CLI + orchestration
- `scraper.py` -> scraping + pagination
- `processor.py` -> cleaning + filtering
- `api.py` -> API calls
- `enricher.py` -> data enrichment
- `writer.py` -> CSV I/O
- `config.py` -> config loader
- `config.json` -> all settings
- `book_data_pipeline.py` -> old version (reference)

Uses logging instead of print.

## Setup

`pip install -r requirements.txt`

## Run

**Note:** Run from the `data_pipeline/` directory.

`python main.py`
`python main.py --help`
`python main.py --input custom.csv --output result.csv`

**Options:**
`--input`   input CSV path (default: from `config.json`)
`--output`  output CSV path (default: from `config.json`)

## What it does

- Scrapes books.toscrape.com
- Retries failed requests
- Follows pagination automatically
- Cleans and filters data
- Matches against input CSV
- Fetches users from API
- Enriches books with user info
- Saves to CSV
- Shows books matched count

## Config

Edit `config.json` to change:
- Scraper settings (URL, delays, retries, timeout)
- Processor settings (max price)
- API settings (URL, timeout)
- Default paths

## Example output

```
title,price,rating,available,user_name,email,company
Book A,15.99,5,True,Leanne Graham,Sincere@april.biz,Romaguera-Crona
```
