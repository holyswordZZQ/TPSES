from model.readAllTeacherInfo import readALLTeacherInfo,getTeacherInfo
import os
from operator import itemgetter
from model.writeTeacherInfo import writeTeacherInfo
from model.readAllTeacherInfo import readAllTeacherID
class operateTeacherInfo:
    def __init__(self):
        self.list=[]


#获取所有老师的信息,getTeacherInfo()返回一个[[]],每一个小列表装着四个信息,id,name,college,title

    def getTeacherInfo(self):
        self.list=readALLTeacherInfo()
        specTeacherInfo=[]
        lspecTeacherInfo=[]

        for i in range(len(self.list)):
            specTeacherInfo.append(self.list[i].get('id'))
            specTeacherInfo.append(self.list[i].get('name'))
            specTeacherInfo.append(self.list[i].get('college'))
            specTeacherInfo.append(self.list[i].get('title'))
            specTeacherInfo.append(self.list[i].get('performance'))
            specTeacherInfo.append(self.list[i].get('time'))
            specTeacherInfo.append(self.list[i].get('available'))
            lspecTeacherInfo.append(specTeacherInfo)
            specTeacherInfo=[]

        return lspecTeacherInfo

#通过ID获取特定一个老师的信息
    def getTeacherInfoDict(self,id):
        fileList=os.listdir('resources/jsons')
        dict={}
        for item in fileList:
            if id+'.json'==item:
                dict=getTeacherInfo(id)
        return dict

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
        finalList=[]
        for dic in self.list:    #采用self.list,省去了读文件的步骤
            if (dic.get('college')==college or college=='全部')and(dic.get('title')==title or title=='全部'):
                firstTempList.append(dic)
        if keyword!='':
            for dic in firstTempList:
                if(dic.get('name').find(keyword)!=-1 or dic.get('id').find(keyword)!=-1):   #模糊了起来
                    secondTempList.append(dic)
        else:
            secondTempList=firstTempList
        print(secondTempList)


        for dic in secondTempList:
            list=[]
            print(dic)
            list.append(dic.get('id'))
            list.append(dic.get('name'))
            list.append(dic.get('college'))
            list.append(dic.get('title'))
            list.append(dic.get('performance'))
            list.append(dic.get('time'))
            list.append(dic.get('available'))
            finalList.append(list)
        return finalList

    def sortByTime(self,data,flag):
        print(data)
        for i in range(len(data)):
            for j in range(0,len(data)-i-1):
                if int(data[j][5])>int(data[j+1][5]):
                    data[j],data[j+1]=data[j+1],data[j]
        if flag==True:
            return data
        else:
            return list(reversed(data))

    def deleteInfo(self,list):
        dict={}
        for item in list:
            dict=self.getTeacherInfoDict(item)
            dict['available']='0'
        writeTeacherInfo(dict)

    def addTeacherInfo(self,d):

        writeTeacherInfo(d)

    def getExistedTeacher(self,id):
        list = readAllTeacherID()
        return id in list

    def modifyTeacherInfo(self,dict):
        writeTeacherInfo(dict)
















