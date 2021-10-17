from model.readOrWriteInExcel import readExcel
from model.teacherInfoModel import teacherInfoModel
import re
import xlwt
import pandas as pd
class operateTeacherInfoByExcelController:
    def __init__(self):
        self.tim=teacherInfoModel()
    def submitInfo(self,filename):
        teacherInfoTable=readExcel(filename)
        idList=list(teacherInfoTable['教师id'])
        nameList=list(teacherInfoTable['教师姓名'])
        collegeList=list(teacherInfoTable['学院'])
        print(collegeList)
        titleList=list(teacherInfoTable['职称'])
        timeList=list(teacherInfoTable['入职时间'])
        repeatedTeacherIDList=[]
        errorTeacherIDList=[]
        i=0  #列表下标
        for id in idList:
            print(i)
            if str(id) in self.tim.getAllTeacherID():
                repeatedTeacherIDList.append(str(id))
                i+=1
                continue
            elif re.match('\d\d\d\d\d\d\d\d',str(id))==None or re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])',str(timeList[i]))==None:
                errorTeacherIDList.append(str(id))
                i+=1
                continue
            else:
                teacherInfoDict={}
                teacherInfoDict['id']=str(idList[i])
                teacherInfoDict['name']=str(nameList[i])
                teacherInfoDict['college']=str(collegeList[i])
                teacherInfoDict['title']=str(titleList[i])
                teacherInfoDict['performance']=[]
                teacherInfoDict['time']=str(timeList[i])
                teacherInfoDict['available']='1'
                self.tim.writeTeacherInfo(teacherInfoDict)
                i+=1
        return repeatedTeacherIDList,errorTeacherIDList

    def exportToExcel(self,data,filename):
        teacherInfoDictList=[]
        for item in data:
            if item[6]=='1':
                teacherInfoDict={}
                teacherInfoDict['id']=item[0]
                teacherInfoDict['name']=item[1]
                teacherInfoDict['college']=item[2]
                teacherInfoDict['title']=item[3]
                teacherInfoDict['time']=item[5]
                teacherInfoDictList.append(teacherInfoDict)
        pf = pd.DataFrame(teacherInfoDictList)
        order = ['id', 'name','college','title','time']
        pf = pf[order]
        tableHead={'id':'教师id','name':'教师姓名','college':'学院','title':'职称','time':'入职时间'}
        pf.rename(columns=tableHead, inplace=True)
        file_path = pd.ExcelWriter(filename)
        pf.fillna(' ', inplace=True)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        file_path.save()



