import os
import json

def writeTeacherInfo(d):
    with open('resources/jsons/{}'.format(d['id'])+'.json','w',encoding='utf-8') as wfile:
        json.dump(d,wfile,ensure_ascii=False)