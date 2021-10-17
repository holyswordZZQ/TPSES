import pandas as pd
def readExcel(filename):
    data=pd.read_excel(filename)
    return data