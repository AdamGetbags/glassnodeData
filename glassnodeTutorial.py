# -*- coding: utf-8 -*-
"""
Glassnode API // Full Python Tutorial 
author: Adam Getbags
"""

#pip install plotly

import json
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
from glassnodeAPIkey import glassnodeAPIkey 

# insert your API key here
API_KEY = 'APIkeyAPIkeyAPIkeyAPIkey'

"""
make API request to get all endpoints
"""
res = requests.get(
    'https://api.glassnode.com/v2/metrics/endpoints',
    params={'api_key': glassnodeAPIkey}
)

# convert to pandas dataframe
endpointData = pd.read_json(res.text)

# review endpoint data
print(endpointData.columns)

# view all endpoint URLs
print(endpointData.path)

# view specific endpoint
print(endpointData.path[0])

# view specific endpoint tier
print(endpointData.tier[0])

# all endpoints for specific tier 
print(endpointData.path[endpointData.tier == 1])

# all endpoints for specific tier AND lower
print(endpointData.path[endpointData.tier <= 2])

# find index/row number of endpoint by path
endpointRow = endpointData[
                endpointData.path == '/v1/metrics/market/price_usd_ohlc']
print(endpointRow)

# supported assets by endpoint // in a DataFrame
print(pd.DataFrame(endpointData.assets[endpointRow.index[0]]))

# view data resolution, granularity
print(endpointData.resolutions[endpointRow.index[0]])

"""
make API request to get candlestick data
"""
# res = requests.get(
#     'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
#     params={'a': 'BTC', 'api_key': glassnodeAPIkey, 'i': '24h'}
# )

# # same request but with 1h resolultion
# # res = requests.get(
# #     'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
# #     params={'a': 'BTC', 'api_key': API_KEY, 'i': '1h'}
# # )

# # convert to pandas dataframe
# candleData = pd.read_json(res.text, convert_dates=['t'])

# # rename columns
# candleData = candleData.rename(columns={'t': 'Date', 'o': 'Candles'})

# # set index to date
# candleData = candleData.set_index('Date')

# # turn candle dictionaries into individual series
# candleData = candleData.Candles.apply(pd.Series)

# # rename columns
# candleData = candleData.rename(columns={'c': 'Close', 'h': 'High', 
#                                         'l': 'Low', 'o': 'Open'})

# # generate plotly figure
# fig = go.Figure(data=[go.Candlestick(x=candleData.index,
#                 open=candleData['Open'],
#                 high=candleData['High'],
#                 low=candleData['Low'],
#                 close=candleData['Close'])])

# # open figure in browser
# plot(fig, auto_open=True)

"""
make request to get total addresses // BTC
"""
# res = requests.get(
#     'https://api.glassnode.com/v1/metrics/addresses/count',
#     params={'a': 'BTC', 'api_key': glassnodeAPIkey}
# )

# # # make request to get total addresses // ETH
# # res = requests.get(
# #     'https://api.glassnode.com/v1/metrics/addresses/count',
# #     params={'a': 'ETH', 'api_key': glassnodeAPIkey}
# # )

# # convert to pandas dataframe
# addressData = pd.read_json(res.text, convert_dates=['t'])

# # rename columns
# addressData = addressData.rename(columns={'t': 'Date', 'v': 'numAddresses'})

# # set index to date
# addressData = addressData.set_index('Date')

# # plot address data
# addressData.plot()

"""
make a request to get Spent Output Profit Ratio // SOPR
"""
# res = requests.get(
#     'https://api.glassnode.com/v1/metrics/indicators/sopr',
#     params={'a': 'BTC', 'api_key': glassnodeAPIkey}
# )

# # convert to pandas dataframe
# soprData = pd.read_json(res.text, convert_dates=['t'])

# # rename columns
# soprData = soprData.rename(columns={'t': 'Date', 'v': 'SOPR'})

# # set index to date
# soprData = soprData.set_index('Date')

# # plot address data
# soprData.plot()

"""
make a request to get % supply last active 1+ years ago
"""

# res = requests.get(
#     'https://api.glassnode.com/v1/metrics/supply/active_more_1y_percent',
#     params={'a': 'BTC', 'api_key': glassnodeAPIkey}
# )

# # convert to pandas dataframe
# supplyData = pd.read_json(res.text, convert_dates=['t'])

# # rename columns
# supplyData = supplyData.rename(columns={'t': 'Date', 'v': 'LongTermSupply'})

# # set index to date
# supplyData = supplyData.set_index('Date')

# # plot address data
# supplyData.plot()

"""
make a request to get pi cycle top data
"""

# res = requests.get(
#     'https://api.glassnode.com/v1/metrics/indicators/pi_cycle_top',
#     params={'a': 'BTC', 'api_key': glassnodeAPIkey}
# )

# # convert to pandas dataframe
# piCycleData = pd.read_json(res.text, convert_dates=['t'])

# # rename columns
# piCycleData = piCycleData.rename(columns={'t': 'Date', 'o': 'movAvgData'})

# # set index to date
# piCycleData = piCycleData.set_index('Date')

# # turn dictionaries into individual series
# piCycleData = piCycleData.movAvgData.apply(pd.Series)

# # plot address data
# piCycleData.plot()
