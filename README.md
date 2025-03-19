# SPY: A data analysis project on a popular ETF

The **goal** of this project is to analyze stock data (ticker: `SPY`) and create a dashboard in Metabase.

## Project Description
### Tools Overview

- **Alpha Vantage**: Free API for historical stock data.
- **DuckDB**: Lightweight, fast, and embedded database for analytical workloads.
- **Metabase**: Open-source BI tool for creating interactive dashboards.

### Steps Overview
1. Fetch historical stock data using Alpha Vantage.
2. Store the data in DuckDB.
3. Connect Metabase to DuckDB.
4. Add current trading price
5. Start with 5 basic interactive plots in Metabase:
    1. How has the closing price of SPY changed over time?
    2. What is the daily trading volume of SPY?
    3. What are the daily price movements?
    4. What is the distribution of daily returns?
    5. How do the 50-day and 200-day moving averages compare?


### Setup

<!-- TODO: TBC-->

Complete this section as you go. Include the following in the `Makefile`:
- [ ] `make environment`
- [ ] `make dataset`
- [ ] `make viz`

## North Star
- [ ] Add N biggest holdings table
- [ ] Compare to individual stocks
- [ ] Technical indicators
- [ ] Correlation analysis
    - Other assets, e.g. Gold, bonds, etc.
    - Macro indicators
- [ ] Sentiment analysis
- [ ] Predictive modeling
