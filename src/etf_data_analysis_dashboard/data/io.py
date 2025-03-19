import os

from dotenv import load_dotenv
from loguru import logger
import pandas as pd
import requests
import yfinance as yf

from etf_data_analysis_dashboard.config import (
    RAW_DATA_PATH,
    START_DATE,
    END_DATE,
    SYMBOL,
)

load_dotenv()


def extract_from_yfinance(*args, **kwargs) -> pd.DataFrame | None:
    """Extract data from Yahoo Finance."""
    DATA_OUT_PATH = RAW_DATA_PATH / "raw_data.csv"

    # Download SPY data
    logger.info("Extracting data from Yahoo Finance...")
    data = yf.download(
        SYMBOL,
        start=START_DATE.strftime("%Y-%m-%d"),
        end=END_DATE.strftime("%Y-%m-%d"),
    )

    if data is not None:
        logger.success("Data extracted successfully.")
        data.to_csv(DATA_OUT_PATH)
        logger.info(f"Data saved locally in {DATA_OUT_PATH}.")

        return data
    else:
        logger.error("Data extraction failed.")
        return None


def extract_from_av_api(ticker: str, *args, **kwargs) -> pd.DataFrame | None:
    """Extract daily historical data using the Alpha Vantage API."""
    # Set up the API request
    API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    FUNCTION = "TIME_SERIES_DAILY"
    URL = f"https://www.alphavantage.co/query?function={FUNCTION}&symbol={ticker}&apikey={API_KEY}&datatype=csv&outputsize=full"
    DATA_OUT_PATH = RAW_DATA_PATH / "raw_data.csv"

    logger.info("Extracting data from the Alpha Vantage API...")

    response = requests.get(URL)
    if response.status_code != 200:
        logger.error(f"Data extraction failed. Response code: {response.status_code}")
        return None

    data = pd.read_csv(URL)

    data.to_csv(DATA_OUT_PATH, index=False)

    logger.info(f"Data saved locally in {DATA_OUT_PATH}.")
    logger.success("Data extracted successfully.")

    return data


if __name__ == "__main__":
    extract_from_av_api(SYMBOL)
