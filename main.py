from readDataBTCTurk import *
from readBinanceData import *
from readCurrencyData import *
import telegram
import time


delay=30
while True:
    try:
        USDTRY=getCurrencyData()
        BinanceData=getBinanceData()
        BTCTurkData=getBTCTurkData()
        message_threshold=0.995
        BTCTurkUSDT=BTCTurkData["USDTTRY"]["ask"]

        print(BTCTurkData.keys())
        print(BinanceData)
        result=list()
        message=""
        for key in BTCTurkData.keys():

            USDTL=BTCTurkUSDT
            if key[:-3]!="USDT" and key[:-3]+"USDT" in BinanceData.keys() :
                binancekey=key[:-3]+"USDT"
                binanceprice=BinanceData[binancekey]["bid"]

                if BTCTurkData[key]["ask"]/USDTL<message_threshold*binanceprice:
                    message= message + "Ratio : "+str(BTCTurkData[key]["ask"]/(USDTL*binanceprice))+"\n"
                    message = message + "BTCTURKte " + key + " fiyatı = " + str(BTCTurkData[key]["ask"]) + " TRY\n"
                    message=message + "BTCTURKte " + key +  " fiyatı = "+str(BTCTurkData[key]["ask"]/USDTL)+ " USD \n"
                    message=message + "Binance " + binancekey +  " fiyatı = "+str(binanceprice)+ " USD \n \n"



                print(binancekey)
                print(binanceprice)
        print(message)
        if len(message)>6:
            message= "USDTRY= " + str(USDTRY)+"\nBTCTurk USDT =" + str(BTCTurkData["USDTTRY"]["ask"]) + "\n\n" + message
            telegram.send_message([message],["emre"],reply_markup=None)
    except:
        telegram.send_message(["Hatasız Bot Olmaz be Emre"], ["emre"], reply_markup=None)


    time.sleep(delay)