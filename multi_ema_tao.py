# %%
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import asyncio
import plotly.graph_objects as go



# %%
last_day =datetime.now()
last_day=last_day.date()
last_day=str(last_day)
last_day

# %%
symbol_analyze="NVDA"


count=1200     # how much candle ?

# %%
#################  download data


def yahoo_symbol(symbol="NVDA",timeframe='1d'):
    while True:
        try:
            data = yf.download(symbol,period='max',interval= timeframe)
            return(data)
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(2)  # Sleep for 10 seconds before retrying




price_data=yahoo_symbol(symbol=symbol_analyze)
price_data

# %%
price_data=price_data.tail(count)

# %%

price_data['ema8']=price_data['Close'].rolling(8).mean()
price_data['ema21']=price_data['Close'].rolling(21).mean()
price_data['ema34']=price_data['Close'].rolling(34).mean()
price_data['ema55']=price_data['Close'].rolling(55).mean()
price_data['ema89']=price_data['Close'].rolling(89).mean()

price_data

# %%
fig = go.Figure(data=[go.Candlestick(x=price_data.index, open=price_data.Open, high=price_data.High, low=price_data.Low, close=price_data.Close)] )
 
 
 
 
fig.add_trace(go.Scatter(x=price_data.index, y=price_data['ema8'], mode='lines', name='sma20', line=dict(color='black')))
fig.add_trace(go.Scatter(x=price_data.index, y=price_data['ema21'], mode='lines', name='ema21', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=price_data.index, y=price_data['ema34'], mode='lines', name='ema34', line=dict(color='lime')))
fig.add_trace(go.Scatter(x=price_data.index, y=price_data['ema55'], mode='lines', name='ema55', line=dict(color='purple'))) 
fig.add_trace(go.Scatter(x=price_data.index, y=price_data['ema89'], mode='lines', name='ema89', line=dict(color='purple'))) 

 
 
fig.update_layout(title = "SYMBOL", xaxis_title = 'Date', yaxis_title = 'Price',width=1200 ,height=700)
 
fig.show()


