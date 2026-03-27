Folder Monitoring Automation

Monitors a folder for new CSV files and automatically cleans them in real-time.

How to run:

Default mode (checks every 5 seconds):
python folder_monitor/monitoring_automation.py

Custom configuration:
python folder_monitor/monitoring_automation.py --input path/to/monitor --output path/to/clean --interval 10

Options:
--input     Path to monitored folder (default: test_files/monitor/)
--output    Path to output folder (default: test_files/clean/)
--interval  Check interval in seconds (default: 5)

What it does:
- Monitors specified folder at regular intervals
- Detects new CSV files
- Cleans data (removes duplicates, standardizes format)
- Saves cleaned files with _clean suffix
- Marks files as processed