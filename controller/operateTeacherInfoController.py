import os
from operator import itemgetter
from model.teacherInfoModel import teacherInfoModel
class operateTeacherInfoController:
    def __init__(self):
        self.list=[]
        self.tim=teacherInfoModel()

#获取所有老师的信息,getTeacherInfo()返回一个[Teacher],每一个Teacher装着对应的信息

    def getTeacherInfo(self):
        self.list=self.tim.readALLTeacherInfo()
        return self.list

#通过ID获取特定一个老师的信息
    def getSingleTeacherInfo(self,id):
        fileList=os.listdir('resources/teacherData')
        if id+'.json' in fileList:
            teacher = self.tim.getTeacherInfo(id)
            return teacher
        else:
            return -1

#获取所有老师的ID
    def getTeacherIDList(self):
        fileList=os.listdir('resources/jsons')
        list=[]
        for item in fileList:
            list.append(item.split('.',1)[0])
        return list


    def getTeacherInfoByConditions(self,keyword,college,title):
        firstTempList=[]
        secondTempList=[]
        for dic in self.list:    #采用self.list,省去了读文件的步骤
            if (dic.college==college or college=='全部')and(dic.title==title or title=='全部'):
                firstTempList.append(dic)
        if keyword!='':
            for dic in firstTempList:
                if(dic.name.find(keyword)!=-1 or dic.id.find(keyword)!=-1):   #模糊了起来
                    secondTempList.append(dic)
        else:
            secondTempList=firstTempList

        return secondTempList

    def sortByTime(self,data,flag):
        print(data)
        for i in range(len(data)):
            for j in range(0,len(data)-i-1):
                if int(data[j].time)>int(data[j+1].time):
                    data[j],data[j+1]=data[j+1],data[j]
        if flag==True:
            return data
        else:
            return list(reversed(data))

    def deleteInfo(self,teacherIDList):
        for id in teacherIDList:
            teacher=self.getSingleTeacherInfo(id)

            dic={
                "id":teacher.id,
                "name":teacher.name,
                "college":teacher.college,
                "title":teacher.title,
                "time":teacher.time,
                "available":'0'
            }
            self.tim.writeTeacherInfo(dic)

    def addTeacherInfo(self,dict):
        self.tim.writeTeacherInfo(dict)


    def modifyTeacherInfo(self,dict):
        self.tim.writeTeacherInfo(dict)
