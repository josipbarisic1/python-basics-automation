import requests
import logging
import sys


logger = logging.getLogger(__name__)

def fetch_data(config):
    api_url = config["url"]
    timeout = config["timeout"]
    try:
        response = requests.get(api_url, timeout = timeout)
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        sys.exit(1)

    if response.status_code != 200:
        logger.error(f"Failed request: {response.status_code}")
        sys.exit(1)
    try:
        data_users = response.json()
    except ValueError:
        logger.error("Failed to parse JSON response")
        sys.exit(1)

    if not isinstance(data_users, list):
        logger.error("Unexpected API format")
        sys.exit(1)

    logger.info(f"Fetched {len(data_users)} users from API")
    return data_users