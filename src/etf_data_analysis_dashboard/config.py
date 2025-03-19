import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw"
PROCESSED_DATA_PATH = DATA_DIR / "processed"

SYMBOLS = ["SPY"]
NUM_YEARS = 2
END_DATE = datetime.datetime.now()
START_DATE = END_DATE - datetime.timedelta(weeks=NUM_YEARS * 52)  # 5 years of data


if __name__ == "__main__":
    print(ROOT_DIR)
