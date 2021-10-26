import datetime
import time
import re
#from model.readPerforID import readPerforID
from model.writeToTxt import writeToTxt
from model.teacherPerformanceModel import teacherPerformanceModel
from entity.performanceEntity.teacherPerformance import teacherPerformance
from model.teacherInfoModel import teacherInfoModel

class operateTeacherPerformController:
    def __init__(self):
        self.tpm=teacherPerformanceModel()
        self.tim=teacherInfoModel()
        self.shownPerformances=[]
        # self.performList=performList
        # self.shownPerformances=self.tpm.getShownTeacherPerformance(self.performList)

    def getShownPerformances(self,IDList):
        self.shownPerformances=self.tpm.getTeacherPerformancesByTeacherID(IDList)
    def getTeacherPerformsByID(self,IDlist,perforID):
        return self.tpm.getTeacherPerformance(performIDList=IDlist,perforID=perforID)

    def turnTeacherIdToPerformIdList(self,teacherIDList):
        return self.tpm.getTeacherPerformIDList(teacherIDList)

    def isIDOrTimeRight(self,textID,textTime):
        reIDState = re.match('\d\d\d\d\d\d\d\d', textID)  # 正则表达式，要求输入的id符合8位数字
        reTimeState = re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])', textTime)
        if reIDState==None or reTimeState==None:
            return 0
        elif textID not in self.tim.getAllTeacherID():
            return 1
        else:
            return 2

    def getCurrentTime(self):
        currentTime=datetime.datetime.now()
        return str(currentTime.year)+str(currentTime.month)+str(currentTime.day)

    def addPerform(self,performDict):
        paperTitle, paperAuthor, paperMoneyAmount, paperJournals, paperIF, \
        monographName, monographBelonged, monographMoneyAmount, \
        prizeName, prizeAwardingCompany, prizeWinner, prizeAmount, \
        projectName, projectRequester, projectPrincipal, projectMoneyAmount, \
        performanceID, type, credit, teacherID, lastUpdateTime, performanceHappenTime, relatedPic, note = \
        performDict.get("paperTitle"), performDict.get("paperAuthor"), performDict.get("paperMoneyAmount"), performDict.get("paperJournals"), performDict.get("paperIF"), \
        performDict.get("monographName"), performDict.get("monographBelonged"), performDict.get("monographMoneyAmount"), \
        performDict.get("prizeName"), performDict.get("prizeAwardingCompany"), performDict.get("prizeWinner"), performDict.get("prizeAmount"), \
        performDict.get("projectName"), performDict.get("projectRequester"), performDict.get("projectPrincipal"), performDict.get("projectMoneyAmount"), \
        performDict.get("performanceID"), performDict.get("type"), performDict.get("credit"), performDict.get("teacherID"), performDict.get("lastUpdateTime"), performDict.get("performanceHappenTime"), performDict.get("relatedPic"), performDict.get("note")

        performance = teacherPerformance(paperTitle, paperAuthor, paperMoneyAmount, paperJournals, paperIF, \
        monographName, monographBelonged, monographMoneyAmount, \
        prizeName, prizeAwardingCompany, prizeWinner, prizeAmount, \
        projectName, projectRequester, projectPrincipal, projectMoneyAmount, \
        performanceID, type, credit, teacherID, lastUpdateTime, performanceHappenTime,relatedPic, note)
        self.tpm.addTeacherPerformance(performance,performanceID)

    def getPerforIDByTxt(self):
        return self.tpm.getTeacherPerforIDByTxt()

    def writePerforIDByTxt(self, a):
        self.tpm.writePerformIDToTxt(str(a))

    def chooseTheExistedValueFromList(self,list):
        for item in list:
            if item!=None and item!='':
                return item
        return '0'

    def getPerformInfoByConditions(self,moneyText,perforTypeText,happenTimeText):
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