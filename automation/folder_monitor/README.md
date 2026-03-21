Folder Monitoring Automation

Monitors a folder for new CSV files and automatically cleans them.

How to run:
python monitoring_automation.py

Input:
Drop CSV files into test_files/monitor/

Output:
Cleaned files appear in test_files/clean/

What it does:
- Runs continuously (checks every 10 seconds)
- Removes duplicates
- Standardizes formatting
- Tracks processed files to avoid reprocessing