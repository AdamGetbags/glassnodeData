# -*- coding: utf-8 -*-
"""

OHLC data from Glassnode API
author: Adam Getbags

"""

import json
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

# insert your API key here
API_KEY = 'APIkeyAPIkeyAPIkeyAPIkey'

# make API request
res = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
                   params={'a': 'BTC', 'api_key': API_KEY, 'i': '24h'})

# res = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
#                    params={'a': 'BTC', 'api_key': API_KEY, 'i': '1h'})

# convert to pandas dataframe
cryptoData = pd.read_json(res.text, convert_dates=['t'])

# rename columns
cryptoData = cryptoData.rename(columns={'t': 'Date', 'o': 'Candles'})

# set index to date
cryptoData = cryptoData.set_index('Date')

# turn candle dictionaries into individual series
cryptoData = cryptoData.Candles.apply(pd.Series)

# rename columns
cryptoData = cryptoData.rename(columns={'c': 'Close', 'h': 'High', 
                                        'l': 'Low', 'o': 'Open'})

#generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=cryptoData.index,
                open=cryptoData['Open'],
                high=cryptoData['High'],
                low=cryptoData['Low'],
                close=cryptoData['Close'])])

#open figure in browser
plot(fig, auto_open=True)