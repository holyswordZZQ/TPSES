import  os
import  json
from entity.performanceEntity.teacherPerformance import teacherPerformance
class teacherPerformanceModel:
    def __init__(self):
        self.performances=self.getAllTeacherPerformances()
    def getAllTeacherPerformances(self):
        performancesList=[]
        fileList = os.listdir("resources/performanceData")
        for filename in fileList:
            with open("resources/performanceData/" + filename, 'r', encoding='utf-8') as f:
                performDict = json.load(f)

                paperTitle, paperAuthor, paperMoneyAmount, paperJournals, paperIF, \
                monographName, monographBelonged, monographMoneyAmount, \
                prizeName, prizeAwardingCompany, prizeWinner, prizeAmount, \
                projectName, projectRequester, projectPrincipal, projectMoneyAmount, \
                performanceID, type, credit, teacherID, lastUpdateTime, performanceHappenTime, relatedPic, note = \
                    performDict.get("paperTitle"), performDict.get("paperAuthor"), performDict.get(
                        "paperMoneyAmount"), performDict.get("paperJournals"), performDict.get("paperIF"), \
                    performDict.get("monographName"), performDict.get("monographBelonged"), performDict.get(
                        "monographMoneyAmount"), \
                    performDict.get("prizeName"), performDict.get("prizeAwardingCompany"), performDict.get(
                        "prizeWinner"), performDict.get("prizeAmount"), \
                    performDict.get("projectName"), performDict.get("projectRequester"), performDict.get(
                        "projectPrincipal"), performDict.get("projectMoneyAmount"), \
                    performDict.get("performanceID"), performDict.get("type"), performDict.get(
                        "credit"), performDict.get("teacherID"), performDict.get("lastUpdateTime"), performDict.get(
                        "performanceHappenTime"), performDict.get("relatedPic"), performDict.get("note")

                performance = teacherPerformance(paperTitle, paperAuthor, paperMoneyAmount, paperJournals, paperIF, \
                monographName, monographBelonged, monographMoneyAmount, \
                prizeName, prizeAwardingCompany, prizeWinner, prizeAmount, \
                projectName, projectRequester, projectPrincipal, projectMoneyAmount, \
                performanceID, type, credit, teacherID, lastUpdateTime,
                performanceHappenTime, relatedPic, note)
                performancesList.append(performance)
        return performancesList

    def getTeacherPerformance(self,performIDList=[],perforID='0'):
        selectedByTeacherIDPerformances=[]
        if perforID=='0':
            for id in performIDList:
                for performance in self.performances:
                    if id==performance.performanceID:
                        selectedByTeacherIDPerformances.append(performance)
            return selectedByTeacherIDPerformances
        else:
            for performance in self.performances:
                if perforID==performance.performanceID:
                    selectedByTeacherIDPerformances.append(performance)
            return selectedByTeacherIDPerformances

    def getShownTeacherPerformance(self,performIDList):
        shownPerformances=[]
        if performIDList!='':
            for id in performIDList:
                for performance in self.performances:
                    if id == performance.performanceID:
                        shownPerformances.append(performance)
        else:
            shownPerformances=self.performances
        return shownPerformances

    def addTeacherPerformance(self,performance,performanceID):
        with open("resources/performanceData/" +performanceID+ '.json','w',encoding='utf-8',) as f:
            dict={
                "performanceID": performance.performanceID,
                "credit": performance.credit,
                "type": performance.type,
                "teacherID": performance.teacherID,
                "lastUpdateTime": performance.lastUpdateTime,
                "performanceHappenTime": performance.performanceHappenTime,
                "relatedPic": performance.relatedPic,
                "note": performance.note,
                "paperTitle": performance.paperTitle,
                "paperAuthor": performance.paperAuthor,
                "paperMoneyAmount": performance.paperMoneyAmount,
                "paperJournals": performance.paperJournals,
                "paperIF": performance.paperIF,
                "monographName": performance.monographName,
                "monographBelonged": performance.monographBelonged,
                "monographMoneyAmount": performance.monographMoneyAmount,
                "prizeName": performance.prizeName,
                "prizeAwardingCompany": performance.prizeAwardingCompany,
                "prizeWinner": performance.prizeWinner,
                "prizeAmount": performance.prizeAmount,
                "projectName": performance.projectName,
                "projectRequester": performance.projectRequester,
                "projectPrincipal": performance.projectPrincipal,
                "projectMoneyAmount": performance.projectMoneyAmount
            }
            json.dump(dict,f)
            #self.performances=self.getAllTeacherPerformances()

    def getTeacherPerforIDByTxt(self):
        with open('resources/txt/perforID.txt', 'r', encoding='utf-8') as rfile:
            teacherID=rfile.read()
            return teacherID

    def writePerformIDToTxt(self,a):
        with open('resources/txt/perforID.txt', 'w', encoding='utf-8') as wfile:
            wfile.write(str(a))

    def getAllTeacherPerformId(self):
        performList=os.listdir('resources/performanceData')
        return performList

    def getTeacherPerformIDList(self,teacherIDList):
        performIDList=[]
        if teacherIDList==[]:
            for performance in self.performances:
                performIDList.append(performance.performanceID)
        else:
            for id in teacherIDList:
                for performance in self.performances:
                    if performance.teacherID==id:
                        performIDList.append(performance.performanceID)
        return performIDList

    def getTeacherPerformancesByTeacherID(self,teacherIDList):
        performanceList=[]
        if teacherIDList==[]:
            for performance in self.performances:
                performanceList.append(performance)
        else:
            for id in teacherIDList:
                for performance in self.performances:
                    if performance.teacherID==id:
                        performanceList.append(performance)
        return performanceList
