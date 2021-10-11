import os
import string
def readPerforID():
    with open('resources/txt/perforID.txt','r',encoding='utf-8') as rfile:
        a=rfile.read()
    print(a)
    return int(a)