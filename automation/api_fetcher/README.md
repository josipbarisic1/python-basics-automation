API Data Fetcher

Fetches user data from a public API and exports it to CSV.

How to run:

Default mode:
python api_fetcher/api_fetcher.py

Custom configuration:
python api_fetcher/api_fetcher.py --output path/to/csv --limit 5

Options:
--output "Path to output file (default: test_files/users_api.csv)"
--limit "Number of users to fetch (default: 10)"

What it does:
- Fetches user data from a public API
- Validates and sanitizes incoming data
- Handles request failures (timeouts, connection errors)
- Safely parses JSON responses
- Handles missing or incomplete fields
- Converts structured JSON into clean CSV output
- Limits number of users (optional)

Example output:

name,email,company,city
Leanne Graham,Sincere@april.biz,Romaguera-Crona,Gwenborough
Ervin Howell,[missing_email],Deckow-Crist,South Elvis