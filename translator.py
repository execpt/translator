import os
import requests
import json
import time
from vardxg import *

os.system('cls')

def banner():
    vardxg = ("""
    Translator V1
    """)
    Write.Print(Center.XCenter(vardxg), Colors.red, interval=0.001)


class translator:
    def __init__(self) -> None:
        pass

    banner()

    text = Write.Input("\n [?] Enter Text >>> ", Colors.purple, interval=0.001)
    language = Write.Input("\n Language -> ", Colors.purple, interval=0.001)
    
    if text == (text) and language == (language):
        url = "https://api.secretprojects.xyz/v1/translator/"
        querystring = {"text":{text},"language":{language}}
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        data = json.loads(response.text)
        status = data['status']
        original = data['original']
        translated = data['translated']

        while True:
            os.system('cls')
            print("\n Status => ", status, Colors.red)
            print("\n Original => ", original, Colors.green)
            print("\n Translated Text => ", translated, Colors.green)
            time.sleep(5)
            os.system('cls')
    else:
        exit

# Made by @vardxg on Telegram!