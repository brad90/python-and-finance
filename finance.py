import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')



# Converting stock data from "yahoo" into a csv

# start = dt.datetime(2000,1,1)
# end = dt.datetime(2016,12,31)
# df = web.DataReader('TSLA', 'yahoo', start, end)
# df.to_csv('tsla.csv')


#  Reading the csv for it to plot.
df = pd.read_csv('tsla.csv', parse_dates = True, index_col=0)
df.index.name = 'Date'
df.shape
df.head(3)
df.tail(3)

# df['Adj Close'].plot()
# plt.show()

# Manipulating the data that is coming form CSV.
# df['100ma']  Create a new column in the CSV file.

# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# print(df.tail())

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

print(df)

# df_ohlc.reset_index(inplace=True)







ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 5, colspan = 1, sharex=ax1)
mpf.plot(df,type='candle')

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

plt.show()
