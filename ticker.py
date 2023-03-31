import pandas as pd
import yfinance as yf
import mplfinance as mpf
class Ticker:
    def __int__( self, symbol, period, subplot, chart_style, style, interval, start ):
        self.symbol = symbol
        self.period = period
        self.history = pd.DataFrame(yf.Ticker(symbol).history(period=period))
        self.volume = True
        self.type = chart_style
        self.style = style


    def plot(self, subplot):
        mpf.plot( self.history,  volume=self.volume, type=self.type, addplot=self.addplot(),  style=self.style )
    def subplot(ticker):
        ticker.history
