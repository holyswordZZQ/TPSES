import json
def readPerforAndCredit():
    with open('resources/material/perfor and credit.json','r',encoding='utf-8') as rfile:
        dict=json.load(rfile)
    return dict