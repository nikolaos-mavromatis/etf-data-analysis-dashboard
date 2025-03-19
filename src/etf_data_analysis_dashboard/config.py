import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw"
PROCESSED_DATA_PATH = DATA_DIR / "processed"

SYMBOL = "SPY"

NUM_YEARS = 2
START_DATE = datetime.datetime(datetime.date.today().year - NUM_YEARS, 1, 1)
END_DATE = datetime.date.today()


if __name__ == "__main__":
    print(ROOT_DIR)
