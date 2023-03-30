import pandas as pd
import mplfinance as mpf
import yfinance as yf


# Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max:
period = "1mo"

# create dataframes from historical ticker data:
dow = pd.DataFrame(yf.Ticker('^DJI').history(period=period))
MSFT = pd.DataFrame(yf.Ticker('MSFT').history(period=period))
AC = pd.DataFrame(yf.Ticker('AC').history(period=period))
AMZN = pd.DataFrame(yf.Ticker('AMZN').history(period=period))
SWTSX = pd.DataFrame(yf.Ticker('SWTSX').history(period=period))

# Plot data using mplfinance:
mpf.plot(dow, volume=True, type="candle")

# create subplots:
subplot = mpf.make_addplot(SWTSX)

# Plot with additional subplot:
mpf.plot(dow, volume=True, type="candle", addplot=subplot, style="yahoo")
