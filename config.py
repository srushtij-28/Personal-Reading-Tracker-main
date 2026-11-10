from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "books.json"

READING_STATUSES = ["To Read", "Reading", "Completed"]
