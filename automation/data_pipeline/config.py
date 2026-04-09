import json
import os
import logging
import sys

logger = logging.getLogger(__name__)

def load_config(config_path=None):
    if config_path is None:
        base_dir = os.path.dirname(__file__)
        config_path = os.path.join(base_dir, "config.json")
    
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        logger.info(f"Loaded config from {config_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config: {e}")
        sys.exit(1)
