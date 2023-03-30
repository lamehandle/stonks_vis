import pandas as pd
import mplfinance as mpf
import yfinance as yf

data = pd.DataFrame([
    {'date': '2019-11-01', 'open': 3050.72, 'high': 3066.95, 'low': 3050.72, 'close': 3066.91, 'volume': 510301237},
    {'date': '2019-11-04', 'open': 3078.96, 'high': 3085.20, 'low': 3074.87, 'close': 3078.27, 'volume': 524848878},
    {'date': '2019-11-05', 'open': 3080.80, 'high': 3083.95, 'low': 3072.15, 'close': 3074.62, 'volume': 585634570},
    {'date': '2019-11-26', 'open': 3134.85, 'high': 3142.69, 'low': 3131.00, 'close': 3140.52, 'volume': 986041660},
    {'date': '2019-11-27', 'open': 3145.49, 'high': 3154.26, 'low': 3143.41, 'close': 3153.63, 'volume': 421853938},
    {'date': '2019-11-29', 'open': 3147.18, 'high': 3150.30, 'low': 3139.34, 'close': 3140.98, 'volume': 286602291},
    ])

buy_price = 0
sell_price = 0

#change 'date' collum into a dateTime object
data.date = pd.to_datetime(data.date)

# change index the date column
data = data.set_index('date')


# plot the data
mpf.plot(data, type="candle", title="CandleStick Chart Test")

# create a subplot to show out sell/buy price


#look into how to use an intersect/ observer in Python
