import pandas as pd
import yfinance as yf


class stock:
    symbol = ''  # string
    data = ''  # A Ticker object using the symbol passed.
    # interval = ''  # data interval (intraday data cannot extend last 60 days)
    # Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo.
    period = ''  # data period to download (Either Use period parameter or use start and end)
    # Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.
    # start = ''  # If not using period - Download start date string (YYYY-MM-DD) or datetime.
    # end = ''  # If not using period - Download end date string (YYYY-MM-DD) or datetime.

    def __init__(self, symbol):
        self.symbol = symbol
        self.data = yf.Ticker(symbol)

    def history(self, period='', start='', end=''):
        if period != '':
            return self.data.history(period=self.period)
        else:
            return self.data.history(start=start, end=end)

    def stock_info(self):
        return self.data.info
