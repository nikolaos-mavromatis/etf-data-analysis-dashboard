import datetime
from pathlib import Path

from loguru import logger
import pandas as pd
from etf_data_analysis_dashboard.config import (
    PROCESSED_DATA_PATH,
    RAW_DATA_PATH,
    NUM_YEARS,
)


def clean_data(input_path: Path | None = None) -> pd.DataFrame:
    """
    Perform the data cleaning steps on the raw DataFrame.

    The goal is to eliminate any missing values and to ensure that the data is ready for analysis and further processing.
    """
    logger.info("Cleaning the data...")
    DATA_IN_PATH = RAW_DATA_PATH / "raw_data.csv" if input_path is None else input_path
    temp = pd.read_csv(
        DATA_IN_PATH,
        skiprows=3,
        index_col="date",
        names=["date", "open", "high", "low", "close", "volume"],
        parse_dates=True,
    )
    DATA_OUT_PATH = PROCESSED_DATA_PATH / "SPY_cleaned.csv"

    temp.columns = temp.columns.str.lower()
    temp.index.name = temp.index.name.lower()
    all_dates = pd.date_range(start=temp.index.min(), end=temp.index.max(), freq="D")
    temp = temp.reindex(all_dates).rename_axis("date")
    temp = temp[str(datetime.date.today().year - NUM_YEARS) :]
    temp["volume"] = temp["volume"].fillna(0)
    temp = temp.ffill()

    # Save locally
    temp.to_csv(DATA_OUT_PATH, index=True)

    logger.success(f"Data cleaned successfully and saved locally in {DATA_OUT_PATH}.")

    return temp


if __name__ == "__main__":
    clean_data()
