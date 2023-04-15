import datetime

import ccxt
import pandas as pd
import matplotlib.pyplot as plt

currency = ccxt.binance()


eth = 'ETH/USDT'
btc = 'BTC/USDT'
timeframe = '1M'

exchange_eth = currency.fetch_ohlcv(eth, timeframe)
exchange_btc = currency.fetch_ohlcv(btc, timeframe)

data_eth = pd.DataFrame(exchange_eth, columns=['Дата', 'Открыт', 'Пиковая', 'Низкий', 'Закрыт', 'Объем'])
data_btc = pd.DataFrame(exchange_btc, columns=['Дата', 'Открыт', 'Пиковая', 'Низкий', 'Закрыт', 'Объем'])

data_btc['Дата'] = pd.to_datetime(data_btc['Дата'], unit='ms')
data_eth['Дата'] = pd.to_datetime(data_btc['Дата'], unit='ms')

data_btc['Открыт'].plot(figsize=(6, 6))
data_eth['Открыт'].plot(figsize=(6, 6))

data_btc.set_index('Дата')
data_eth.set_index('Дата')

prices_eth = data_eth[['Открыт', 'Закрыт']]
prices_btc = data_btc[['Открыт', 'Закрыт']]

movement = (prices_eth['Закрыт'] - prices_eth['Открыт']) - (prices_btc['Закрыт'] - prices_btc['Открыт'])


plt.plot(movement, color='blue')
plt.title('Движение цены фьючерса ETHUSDT исключая BTCUSDT')
plt.xlabel('Дата')
plt.ylabel('Движение цены')
# plt.grid(False)
plt.show()
