# Dynamic Web Scraper

**Problem:**  
Need to scrape all pages from a website, but don't know how many pages exist.

**Solution:**  
Automatically follows pagination links, scrapes all pages until no more exist.

## Setup

`pip install -r requirements.txt`

## Run

**Note:** Run from the `web_scraper_dynamic/` directory.

```
python dynamic_scraper.py
python dynamic_scraper.py --help
python dynamic_scraper.py --output custom.csv
```

**Options:**
`--output`  output CSV (default: `test_files/clean_books.csv`)

## What it does

- Scrapes all pages automatically
- Follows "next page" links
- Uses browser-like headers
- Retries failed requests (3x)
- Stops if page fails (fail-fast)
- Adds delay between requests
- Filters by rating (4-5 stars)
- Filters by price (under £20)
- Exports to CSV
- Shows books scraped count

## Output

`test_files/clean_books.csv`
