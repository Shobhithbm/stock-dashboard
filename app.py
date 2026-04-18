import streamlit as st
import yfinance as yf

st.title("📈 Live Stock Dashboard")

# ✅ Dropdown instead of typing
stock = st.selectbox(
    "Select Stock",
    ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]
)

with st.spinner("Fetching live data..."):
    data = yf.download(stock, period="1d", interval="1m")

if data.empty:
    st.error("No data found.")
else:
    close_data = data['Close']

    # Handle empty or invalid data safely
    if close_data.empty:
        st.error("No price data available.")
    else:
        latest_price = close_data.dropna().iloc[-1]

        st.metric("Latest Price", f"{latest_price:.2f}")
        st.line_chart(close_data)
