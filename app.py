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
    # Ensure we always get a proper Series
    close_data = data.get('Close')

    if close_data is None:
        st.error("Close data not found.")
    else:
        # Convert to Series if needed
        if hasattr(close_data, "columns"):
            close_data = close_data.squeeze()

        close_data = close_data.dropna()

        if close_data.empty:
            st.error("No valid data found.")
        else:
            latest_price = close_data.iloc[-1]

            st.metric("Latest Price", round(latest_price, 2))
            st.line_chart(close_data)
