import sys

import pandas as pd
import xlwt
import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget

'''data=pd.read_excel('C:/Users/张子健/githubRepos/GitHub/TPSES/resources/teacherInfoExcel/教师信息.xlsx')
print(data)
print(list(data))
print('-------------------------')
print(list(data['教师id']))
list=data['教师id'].unique()
print(type(list))
print('-------------------------')
print(type(list[0]))
print(str(list[0]))'''

'''list=[{'id':2131,'name':'sdasd','num':4},{'id':2131,'name':'sdasd','num':4},{'id':2131,'name':'sdasd','num':4},{'id':2131,'name':'sdasd','num':4}]
pf=pd.DataFrame(list)
order=['id','num']
pf=pf[order]
file_path = pd.ExcelWriter('../resources/teacherInfoExcel/name2.xlsx')
#替换空单元格
pf.fillna(' ',inplace = True)
#输出
pf.to_excel(file_path,encoding = 'utf-8',index = False)
#保存表格
file_path.save()'''
print(str(sys.maxsize))