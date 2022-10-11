# -*- coding: utf-8 -*-
"""
Glassnode API // Full Pytohn Tutorial 
author: Adam Getbags
"""

import json
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
from glassnodeAPIkey import glassnodeAPIkey 

# insert your API key here
API_KEY = 'APIkeyAPIkeyAPIkeyAPIkey'

"""
make API request to get candlestick data
"""
res = requests.get(
    'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
    params={'a': 'BTC', 'api_key': glassnodeAPIkey, 'i': '24h'}
)

# same request but with 1h resolultion
# res = requests.get(
#     'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
#     params={'a': 'BTC', 'api_key': API_KEY, 'i': '1h'}
# )

# convert to pandas dataframe
candleData = pd.read_json(res.text, convert_dates=['t'])

# rename columns
candleData = candleData.rename(columns={'t': 'Date', 'o': 'Candles'})

# set index to date
candleData = candleData.set_index('Date')

# turn candle dictionaries into individual series
candleData = candleData.Candles.apply(pd.Series)

# rename columns
candleData = candleData.rename(columns={'c': 'Close', 'h': 'High', 
                                        'l': 'Low', 'o': 'Open'})

# generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=candleData.index,
                open=candleData['Open'],
                high=candleData['High'],
                low=candleData['Low'],
                close=candleData['Close'])])

# open figure in browser
plot(fig, auto_open=True)