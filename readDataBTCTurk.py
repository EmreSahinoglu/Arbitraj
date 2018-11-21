import requests
import json

def getBTCTurkData():
    headers=dict()
    headers["user-agent"] = "Mozilla/5.0"

    BTCTurk_ticker_url="https://www.btcturk.com/api/ticker"
    resp = requests.get(url=BTCTurk_ticker_url, headers=headers, params=None, data=None)

    BTCTurkRawData=resp.json()
    BTCTurkData=dict()
    for data in BTCTurkRawData:
        pair=data["pair"]
        BTCTurkData[pair]={}
        BTCTurkData[pair]["bid"]=data["bid"]
        BTCTurkData[pair]["ask"] = data["ask"]
    # print(BTCTurkRawData)
    # print(BTCTurkData)
    return BTCTurkData