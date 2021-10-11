import json
def readPerforAndCredit():
    with open('resources/jsons1/perfor and credit.json','r',encoding='utf-8') as rfile:
        dict=json.load(rfile)
    return dict