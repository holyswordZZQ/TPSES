import pandas as pd
def readExcel(filename):
    print("in readExcel")
    print(filename)
    data=pd.read_excel(filename)
    print("after readExcel")
    return data