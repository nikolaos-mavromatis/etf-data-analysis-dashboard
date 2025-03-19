"""
This module prepares the data for visualization. It extracts the data from the Alpha Vantage API and cleans it.
"""

from etf_data_analysis_dashboard.config import SYMBOL
from etf_data_analysis_dashboard.data.io import extract_from_av_api
from etf_data_analysis_dashboard.data.clean_data import clean_data


def prepare_data_for_viz(extract: bool = False) -> None:
    """Prepare the data for visualization."""
    if extract:
        extract_from_av_api(SYMBOL)
    clean_data()


if __name__ == "__main__":
    prepare_data_for_viz(extract=True)
