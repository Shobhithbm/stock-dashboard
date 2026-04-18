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
    close_data = data['Close'].dropna()

    if len(close_data) == 0:
        st.error("No valid data found.")
    else:
        latest_price = close_data.iloc[-1]

        try:
            latest_price = float(latest_price)
            st.metric("Latest Price", f"{latest_price:.2f}")
        except:
            st.error("Error reading latest price")

        st.line_chart(close_data)
