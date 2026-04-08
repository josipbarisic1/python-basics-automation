Folder Monitor

Monitors folder, auto-processes new CSVs.

Run:

python monitoring_automation.py
python monitoring_automation.py --input monitor/ --output clean/ --interval 10

Options:
--input     monitored folder (default: test_files/monitor/)
--output    output folder (default: test_files/clean/)
--interval  check interval in seconds (default: 5)

What it does:
- Monitors folder continuously
- Detects new CSVs
- Cleans data (removes duplicates, standardizes)
- Saves with _clean suffix
- Marks as processed
