"""JSON file storage."""
import json
import os

from config import DATA_FILE, DEFAULT_RATE


def _empty():
    return {"rate_per_unit": DEFAULT_RATE, "appliances": []}


def load_data():
    if not os.path.exists(DATA_FILE):
        return _empty()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        data.setdefault("rate_per_unit", DEFAULT_RATE)
        data.setdefault("appliances", [])
        return data
    except (json.JSONDecodeError, OSError):
        print("Warning: data file unreadable, starting fresh.")
        return _empty()


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
