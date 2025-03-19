# SPY: A data analysis project on a popular ETF

The **goal** of this project is to analyze stock data (ticker: `SPY`) and create a Streamlit dashboard.

## Project Description
### Tools Overview

- **Alpha Vantage**: Free API for historical stock data.
- **Plotly**: Open-source data visualization library for beautiful, interactive dashboards. 
- **Streamlit**: Open-source tool for creating web apps. Integrates seamlessly with Plotly.

### Steps Overview
- [x] Fetch historical stock data using Alpha Vantage.
- [ ] Add current trading price
- [x] Start with 5 basic interactive plots:
    1. How has the closing price of SPY changed over time?
    2. What is the daily trading volume of SPY?
    3. What are the daily price movements?
    4. What is the distribution of daily returns?
    5. How do the 50-day and 200-day moving averages compare?


## Setup

### Get an Alpha Vantage API Key
Sign up for a free API key at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

### Run the Streamlit server
From the root of the project, execute:

```bash
streamlit run src/app.py
```

<!-- TODO: Complete Makefile

Complete this section as you go. Include the following in the `Makefile`:
- [ ] `make environment`
- [ ] `make dataset`
- [ ] `make viz`
-->

## North Star
- [ ] Add N biggest holdings table
- [ ] Compare to individual stocks
- [ ] Technical indicators
- [ ] Correlation analysis
    - Other assets, e.g. Gold, bonds, etc.
    - Macro indicators
- [ ] Sentiment analysis
- [ ] Predictive modeling
