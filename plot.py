import plotly.graph_objects as go  # MOre complex usage .express utilizes this module under the hood
import plotly.offline as pyo  # allows for offline usage
import stock as st  # Wrapper for yfinance
import yfinance as yf
# pyo.init_notebook_mode()

period = "1mo"  # Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max:

# dow_raw.history(period)

dow_raw = st.stock("^DJI")
dow = yf.Ticker("^DJI").history(period)  # This data works todo refactor to use reset index properly
print(dow)
dow2 = dow.reset_index()  # This works because reset_index returns a new dataframe!!!!!
print(dow2)
# # Plot a candle stick plot with plotly
fig = go.Figure(data=[go.Candlestick(x=dow2['Date'],
                                     open=dow2['Open'],
                                     high=dow2['High'],
                                     low=dow2['Low'],
                                     close=dow2['Close'],
                                     )])
fig.show()
