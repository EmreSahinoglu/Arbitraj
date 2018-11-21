import requests
import json
import urllib


TOKEN = "521808069:AAHoofJk7rvd5c1bznkVtkocETcRG4vhhM4"
chatids={"emre":"253627635","ismail":"542498845","enes":"435747953","denizhan":"536911048","onursagır":"481955496",
         "canberk":"451249758", "mustafa":"439523955"}
# emre="253627635"
# ismail="542498845"
# enes="435747953"
# denizhan="536911048" #Denizhan
# OnurSagır="481955496" #Onur Sağır
# canberk="451249758"
# mustafa="439523955"

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def request(method, path, params=None):
    resp = requests.request(method, path, params=params)
    return resp.json()


def gettickers(str):
    # print(str)
    data = request("GET", str)
    return data


def send_message(textlist, alıcılar, reply_markup=None):
    for alıcı in alıcılar:
        for text in textlist:

            text = urllib.parse.quote_plus(text)
            url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chatids[alıcı])
            if reply_markup:
                url += "&reply_markup={}".format(reply_markup)
            get_url(url)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content