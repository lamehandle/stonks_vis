import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
import yfinance as yf
import stock as st
# import mplfinance as mpf
pyo.init_notebook_mode()

period = "1mo"
# Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max:

dow = st.stock("^DJI")
dow_hist = dow.data.history(period)

# Plot with additional subplot:
mpf.plot(dow, volume=True, type="candle", addplot=subplot, style="yahoo")

# df = yf.Ticker('AMZN').history(period='1mo')
fig = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close']
        ),
    ]
)

fig.show()