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
    latest_price = float(data['Close'].iloc[-1])

    st.metric("Latest Price", f"{latest_price:.2f}")
    st.line_chart(data['Close'])

    # ✅ Download button
    st.download_button(
        label="Download Data as CSV",
        data=data.to_csv(),
        file_name=f"{stock}_data.csv",
        mime="text/csv"
    )