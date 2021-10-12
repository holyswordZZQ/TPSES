from model.readAllTeacherInfo import readALLTeacherInfo,getTeacherInfo
import os

class operateTeacherInfo:
    def __init__(self):
        self.list=[]


#获取所有老师的信息
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
            lspecTeacherInfo.append(specTeacherInfo)
            specTeacherInfo=[]

        return lspecTeacherInfo
# getTeacherInfo()返回一个[[]],每一个小列表装着四个信息,id,name,college,title

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

#精确搜索老师信息
    # def searchTeaherInfo(self,keyword):
    #     teachers=self.list
    #     findedTeacher=[]
    #     searchedTeacherData=[]
    #     for i in range(len(teachers)):
    #         if keyword == teachers[i].get('id') or keyword == teachers[i].get('name'):
    #             findedTeacher.append(teachers[i])   #findedteacher中的元素还是一个字典
    #     for i in range(len(findedTeacher)):    #将一个字典中的元素全部放在一个新列表中
    #         tempArray=[]
    #         tempArray.append(findedTeacher[i].get('id'))
    #         tempArray.append(findedTeacher[i].get('name'))
    #         tempArray.append(findedTeacher[i].get('college'))
    #         tempArray.append(findedTeacher[i].get('title'))
    #         searchedTeacherData.append(tempArray)   #列表内部嵌套一个列表
    #     return searchedTeacherData
    #
    # def getTeacherByAttribute(self,dict,data):
    #     finalTeacherList=[]
    #     print(dict)
    #     if dict['college']=='全部' and dict['title']=='全部':
    #         for item in data:
    #             teachersList = []
    #             teachersList.append(item[0])
    #             teachersList.append(item[1])
    #             teachersList.append(item[2])
    #             teachersList.append(item[3])
    #             finalTeacherList.append(teachersList)
    #         return finalTeacherList
    #     elif dict['college']=='全部':
    #         for item in data:
    #             if item[3]==dict['title']:
    #                 teachersList=[]
    #                 teachersList.append(item[0])
    #                 teachersList.append(item[1])
    #                 teachersList.append(item[2])
    #                 teachersList.append(item[3])
    #                 finalTeacherList.append(teachersList)
    #         return finalTeacherList
    #     elif dict['title']=='全部':
    #         for item in data:
    #             if item[2]==dict['college']:
    #                 teachersList=[]
    #                 teachersList.append(item[0])
    #                 teachersList.append(item[1])
    #                 teachersList.append(item[2])
    #                 teachersList.append(item[3])
    #                 finalTeacherList.append(teachersList)
    #         return finalTeacherList
    #     else:
    #         for item in data:
    #             if item[2]==dict['college'] and item[3]==dict['title']:
    #                 teachersList = []
    #                 teachersList.append(item[0])
    #                 teachersList.append(item[1])
    #                 teachersList.append(item[2])
    #                 teachersList.append(item[3])
    #                 finalTeacherList.append(teachersList)
    #         return finalTeacherList

    def getTeacherInfoByConditions(self,keyword,college,title):
        firstTempList=[]
        secondTempList=[]
        finalList=[]
        for dic in self.list:    #采用self.list,省去了读文件的步骤
            if (dic.get('college')==college or college=='全部')and(dic.get('title')==title or title=='全部'):
                firstTempList.append(dic)
        print(firstTempList)
        if keyword!='':
            for dic in firstTempList:
                if(dic.get('name').find(keyword)!=-1 or dic.get('id').find(keyword)!=-1):
                    secondTempList.append(dic)
        else:
            secondTempList=firstTempList
        print(secondTempList)


        for dic in secondTempList:
            list=[]
            list.append(dic.get('id'))
            list.append(dic.get('name'))
            list.append(dic.get('college'))
            list.append(dic.get('title'))
            finalList.append(list)
        return finalList

    def sortByTime(self,data):
        















