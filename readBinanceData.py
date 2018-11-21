import requests
import json

def getBinanceData():
    binance_ticker_url="https://www.binance.com/api/v3/ticker/bookTicker"
    resp = requests.get(url=binance_ticker_url, headers=None, params=None, data=None).json()
    # print(resp)
    binanceData=dict()

    for data in resp:
        pair=data["symbol"]
        binanceData[pair]=dict()
        binanceData[pair]["bid"]= float(data["bidPrice"])
        binanceData[pair]["ask"] = float(data["askPrice"])


    # print(binanceData["BTCUSDT"])
    return binanceData
