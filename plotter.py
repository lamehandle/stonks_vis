import plotly.graph_objects as go
from stock import stock


class plotter:
    def __int__(self, stock):
        self.stock = stock.reset_index()

    def plot(self):
        fig = go.Figure(data=[go.Candlestick(x=self.stock['Date'],
                                         open=self.stock['Open'],
                                         high=self.stock['High'],
                                         low=self.stock['Low'],
                                         close=self.stock['Close'],
        )])
        fig.show()
