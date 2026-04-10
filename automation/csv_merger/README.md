CSV Merger

Merges multiple monthly CSVs into one, sorted chronologically.

Run:

python csv_merger.py
python csv_merger.py --help
python csv_merger.py --input folder/ --output merged.csv

Options:
--input   folder with CSVs (default: test_files/)
--output  merged CSV (default: test_files/merged_sales.csv)

Input format:
Files named: sales_january.csv, sales_february.csv, etc.

Output:
Shows files merged and total rows processed.
