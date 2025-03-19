import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from etf_data_analysis_dashboard.config import PROCESSED_DATA_PATH, START_DATE, END_DATE

# TODO: Update the path to enhanced data
DATA_IN_PATH = PROCESSED_DATA_PATH / "SPY_cleaned.csv"

# Set up the Streamlit app
st.set_page_config(page_title="Stock Data Dashboard", layout="wide")
st.title("📊 Stock Data Visualization: SPY")

data = pd.read_csv(DATA_IN_PATH)

# Convert 'date' to datetime
data["date"] = pd.to_datetime(data["date"])

# Filter area for user input
with st.expander("Open filters"):
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "Start Date", data["date"].min(), min_value=START_DATE, max_value=END_DATE
        )
    with col2:
        end_date = st.date_input(
            "End Date", data["date"].max(), min_value=START_DATE, max_value=END_DATE
        )


# Filter data based on user input
filtered_data = data[
    (data["date"] >= pd.to_datetime(start_date))
    & (data["date"] <= pd.to_datetime(end_date))
]

# Display raw data
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(filtered_data)

# Plot 1: Closing Price Over Time
st.subheader("How has the closing price of SPY changed over time?")
fig1 = px.line(filtered_data, x="date", y="close", title="SPY Closing Price")
fig1.update_layout(xaxis_title="", yaxis_title="Close Price (USD)")
st.plotly_chart(fig1, use_container_width=True)

# Plot 2: Daily Trading Volume
st.subheader("Daily Trading Volume")
fig2 = px.bar(filtered_data, x="date", y="volume", title="SPY Daily Trading Volume")
st.plotly_chart(fig2, use_container_width=True)

# Plot 3: Candlestick Chart (Open, High, Low, Close)
st.subheader("Candlestick Chart")
fig3 = go.Figure(
    data=go.Candlestick(
        x=filtered_data["date"],
        open=filtered_data["open"],
        high=filtered_data["high"],
        low=filtered_data["low"],
        close=filtered_data["close"],
    )
)
fig3.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig3, use_container_width=True)

# Plot 4: Daily Returns Distribution
st.subheader("Daily Returns Distribution")
filtered_data["daily_return"] = (
    filtered_data["close"] - filtered_data["open"]
) / filtered_data["open"]
fig4 = go.Figure(
    data=[go.Histogram(x=filtered_data["daily_return"], nbinsx=50, histnorm="percent")]
)
fig4.update_layout(title="SPY Daily Returns Distribution")
st.plotly_chart(fig4, use_container_width=True)

# Plot 5: Moving Averages (50-day and 200-day)
st.subheader("Moving Averages")
filtered_data["ma_50"] = filtered_data["close"].rolling(window=50).mean()
filtered_data["ma_200"] = filtered_data["close"].rolling(window=200).mean()
fig5 = go.Figure(
    data=[
        go.Line(x=filtered_data["date"], y=filtered_data["close"], name="Close"),
        go.Line(x=filtered_data["date"], y=filtered_data["ma_50"], name="50-day MA"),
        go.Line(x=filtered_data["date"], y=filtered_data["ma_200"], name="200-day MA"),
    ]
)
st.plotly_chart(fig5, use_container_width=True)
