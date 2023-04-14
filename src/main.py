import asyncio
import datetime
import json

import requests
import websockets

from src.settings import WSS_URL, HTTPS_URL


async def get_first_data():
    response = requests.get(HTTPS_URL)
    price = json.loads(response.text)['price']
    now = datetime.datetime.now()
    return float(price), now


async def get_eth():
    async with websockets.connect(WSS_URL) as client:
        first, start = await get_first_data()
        while True:
            data = json.loads(await client.recv())['data']
            price = data['k']['c']
            print("Новая цена: ", float(price), "|", "Старая цена: ", first, "|",
                  f"Изменение цены за {start} -> ", str(round((abs(first - float(price)) * 100) / first, 3))+'%')
            print((start + datetime.timedelta(minutes=5)).time(), "|", datetime.datetime.now().time())
            print("_"*90)
            if (start + datetime.timedelta(minutes=5)).time() > datetime.datetime.now().time() and (
                    abs(first - float(price)) * 100) / first > 0.01:
                print("Внимание!!! изменение цены более чем на 1%")
                first, start = await get_first_data()


loop = asyncio.run(get_eth())
