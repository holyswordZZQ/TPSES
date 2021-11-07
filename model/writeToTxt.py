
def writeToTxt(a):
    with open('resources/txt/perforID.txt','w',encoding='utf-8') as wfile:
        wfile.write(str(a))