import datetime
import time
import re
#from model1.readPerforID import readPerforID
#from model1.writeToTxt import writeToTxt
from model.teacherPerformanceModel import teacherPerformanceModel
from entity.performanceEntity.teacherPerformance import teacherPerformance
from model.teacherInfoModel import teacherInfoModel
import pandas as pd

class operateTeacherPerformController:
    def __init__(self):
        self.tpm=teacherPerformanceModel()
        self.tim=teacherInfoModel()
        self.shownPerformances=[]  #本层维护一个要展示的业绩对象

    def getShownPerformances(self,IDList):  #获取要展示的业绩对象
        self.shownPerformances=self.tpm.getTeacherPerformancesByTeacherID(IDList)

    def getTeacherPerformsByID(self,IDlist,perforID):   #此方法分为两种模式，第一种：输入业绩ID列表时，输出所对应的业绩对象列表；第二种：输入一个业绩ID返回一个业绩对象
        return self.tpm.getTeacherPerformance(performIDList=IDlist,perforID=perforID)

    def turnTeacherIdToPerformIdList(self,teacherIDList):   #将教师ID转化为业绩ID
        return self.tpm.getTeacherPerformIDList(teacherIDList)

    def isIDOrTimeRight(self,textID,textTime):   #通过正则表达式判断输入的ID以及时间是否符合规范
        reIDState = re.match('\d\d\d\d\d\d\d\d', textID)  # 正则表达式，要求输入的id符合8位数字
        reTimeState = re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])', textTime)
        if reIDState==None or reTimeState==None:
            return 0
        elif textID not in self.tim.getAllTeacherID():
            return 1
        else:
            return 2

    def getCurrentTime(self):  #获取系统当前时间，并以20160101的方式来展现
        currentTime=datetime.datetime.now()
        return str(currentTime.year)+str(currentTime.month)+str(currentTime.day)

    def addPerform(self,performDict):   #添加业绩
        paperTitle, paperAuthor, paperTime, paperJournals, \
        monographName, monographBelonged, monographNumber,monographTime, \
        prizeName, prizeAwardingCompany, prizeProject,\
        bookNanme,bookPublisher,bookISBN,bookTime,\
        projectName, projectType, projectIncharge, projectApplerRole,projectTime, \
        performanceID, type, credit, teacherID, lastUpdateTime,relatedPic, note = \
        performDict.get("paperTitle"), performDict.get("paperAuthor"), performDict.get("paperTime"), performDict.get("paperJournals"), \
        performDict.get("monographName"), performDict.get("monographBelonged"), performDict.get("monographNumber"),performDict.get("monographTime"), \
        performDict.get("prizeName"), performDict.get("prizeAwardingCompany"), performDict.get("prizeProject"),\
        performDict.get("projectName"), performDict.get("projectType"), performDict.get("projectIncharge"), performDict.get("projectApplerRole"),performDict.get("projectTime"), \
        performDict.get('bookName'),performDict.get('bookPublisher'),performDict.get('bookISBN'),performDict.get('bookTime'),\
        performDict.get("performanceID"), performDict.get("type"), performDict.get("credit"), performDict.get("teacherID"), performDict.get("lastUpdateTime"),  performDict.get("relatedPic"), performDict.get("note")

        performance = teacherPerformance(paperTitle, paperAuthor, paperTime, paperJournals, \
        monographName, monographBelonged, monographNumber,monographTime, \
        prizeName, prizeAwardingCompany, prizeProject,\
        bookNanme,bookPublisher,bookISBN,bookTime,\
        projectName, projectType, projectIncharge, projectApplerRole,projectTime, \
        performanceID, type, credit, teacherID, lastUpdateTime,relatedPic, note)
        self.tpm.addTeacherPerformance(performance,performanceID)

    def getPerforIDByTxt(self):
        return self.tpm.getTeacherPerforIDByTxt()

    def writePerforIDByTxt(self, a):
        self.tpm.writePerformIDToTxt(str(a))

    def chooseTheExistedValueFromList(self,list):   #从一个列表中获取存在值的那一项，如果都不存在值，返回0，用以判断每个业绩对象的4种金额中，取存在的那一个
        for item in list:
            if item!=None and item!='':
                return item
        return '0'

    def getPerformInfoByConditions(self,moneyText,perforTypeText,happenTimeText):   #在3种筛选条件之下，返回符合条件的业绩ID列表
        conditionedPerformList=[]
        performancesList=self.shownPerformances

        for performance in performancesList:
            perforMoneyList=[performance.monographMoneyAmount,performance.paperMoneyAmount,performance.projectMoneyAmount,performance.prizeAmount]
            #print(perforMoneyList)
            #print(self.chooseTheExistedValueFromList(perforMoneyList))
            if (int(moneyText.split('-',1)[0])<=int(self.chooseTheExistedValueFromList(perforMoneyList))<int(moneyText.split('-',1)[1])\
            or moneyText=='0-0') and (performance.type==perforTypeText or perforTypeText=='全部') and \
            (int(happenTimeText.split('-',1)[0])<=int(performance.performanceHappenTime)<int(happenTimeText.split('-',1)[1]) or happenTimeText=='0-0'):
                conditionedPerformList.append(performance.performanceID)
        return conditionedPerformList

    def exportPerformToExcel(self,performanceIDList,filename):
        performData=self.tpm.getTeacherPerformance(performIDList=performanceIDList,perforID='0')
        performInfoDictList=[]
        for performance in performData:
            performInfoDict={}
            performInfoDict['performanceID']=performance.performanceID
            performInfoDict['type']=performance.type
            performInfoDict['credit']=performance.credit
            performInfoDict['teacherID']=performance.teacherID
            performInfoDict['lastUpdateTime']=performance.lastUpdateTime
            performInfoDict['note']=performance.note
            if performance.type=='论文':
                performInfoDict['paperTitle']=performance.paperTitle
                performInfoDict['paperAuthor']=performance.paperAuthor
                performInfoDict['paperTime']=performance.paperTime
                performInfoDict['paperJournals']=performance.paperJournals
                performInfoDict['monographName']='无'
                performInfoDict['monographBelonged']='无'
                performInfoDict['monographNumber']='无'
                performInfoDict['monographTime']='无'
                performInfoDict['prizeName']='无'
                performInfoDict['prizeAwardingCompany']='无'
                performInfoDict['prizeWinner']='无'
                performInfoDict['prizeAmount']='无'
                performInfoDict['projectName']='无'
                performInfoDict['projectRequester']='无'
                performInfoDict['projectPrincipal']='无'
                performInfoDict['projectMoneyAmount']='无'
            elif performance.type=='软著':
                performInfoDict['paperTitle'] = '无'
                performInfoDict['paperAuthor'] = '无'
                performInfoDict['paperMoneyAmount'] = '无'
                performInfoDict['paperJournals'] = '无'
                performInfoDict['paperIF'] = '无'
                performInfoDict['monographName'] = performance.monographName
                performInfoDict['monographBelonged'] = performance.monographBelonged
                performInfoDict['monographMoneyAmount'] = performance.monographMoneyAmount
                performInfoDict['prizeName'] = '无'
                performInfoDict['prizeAwardingCompany'] = '无'
                performInfoDict['prizeWinner'] = '无'
                performInfoDict['prizeAmount'] = '无'
                performInfoDict['projectName'] = '无'
                performInfoDict['projectRequester'] = '无'
                performInfoDict['projectPrincipal'] = '无'
                performInfoDict['projectMoneyAmount'] = '无'
            elif performance.type=='获奖':
                performInfoDict['paperTitle'] = '无'
                performInfoDict['paperAuthor'] = '无'
                performInfoDict['paperMoneyAmount'] = '无'
                performInfoDict['paperJournals'] = '无'
                performInfoDict['paperIF'] = '无'
                performInfoDict['monographName'] = '无'
                performInfoDict['monographBelonged'] = '无'
                performInfoDict['monographMoneyAmount'] = '无'
                performInfoDict['prizeName'] = performance.prizeName
                performInfoDict['prizeAwardingCompany'] = performance.prizeAwardingCompany
                performInfoDict['prizeWinner'] = performance.prizeWinner
                performInfoDict['prizeAmount'] = performance.prizeAmount
                performInfoDict['projectName'] = '无'
                performInfoDict['projectRequester'] = '无'
                performInfoDict['projectPrincipal'] = '无'
                performInfoDict['projectMoneyAmount'] = '无'
            elif performance.type=='项目':
                performInfoDict['paperTitle'] = '无'
                performInfoDict['paperAuthor'] = '无'
                performInfoDict['paperMoneyAmount'] = '无'
                performInfoDict['paperJournals'] = '无'
                performInfoDict['paperIF'] = '无'
                performInfoDict['monographName'] = '无'
                performInfoDict['monographBelonged'] = '无'
                performInfoDict['monographMoneyAmount'] = '无'
                performInfoDict['prizeName'] = '无'
                performInfoDict['prizeAwardingCompany'] = '无'
                performInfoDict['prizeWinner'] = '无'
                performInfoDict['prizeAmount'] = '无'
                performInfoDict['projectName'] = performance.projectName
                performInfoDict['projectRequester'] = performance.projectRequester
                performInfoDict['projectPrincipal'] = performance.projectPrincipal
                performInfoDict['projectMoneyAmount'] = performance.projectMoneyAmount

            performInfoDictList.append(performInfoDict)
        pf=pd.DataFrame(performInfoDictList)
        order=['performanceID','type','credit','teacherID','lastUpdateTime','performanceHappenTime','note','paperTitle','paperAuthor','paperMoneyAmount','paperJournals','paperIF','monographName','monographBelonged','monographMoneyAmount','prizeName','prizeAwardingCompany','prizeWinner','prizeAmount','projectName','projectRequester','projectPrincipal','projectMoneyAmount']
        pf=pf[order]
        file_path = pd.ExcelWriter(filename)
        pf.fillna(' ', inplace=True)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        workSheet = file_path.sheets['Sheet1']
        workSheet.set_column('A:W',20)
        file_path.save()


