import requests
import json

def getCurrencyData():
    url="http://free.currencyconverterapi.com/api/v5/convert?q=USD_TRY"
    resp = requests.get(url=url, headers=None, params=None, data=None).json()
    USD_TRY=float(resp["results"]["USD_TRY"]["val"])
    # print(USD_TRY)
    return USD_TRY