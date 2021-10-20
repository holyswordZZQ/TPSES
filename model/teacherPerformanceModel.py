import  os
import  json
from entity.performanceEntity.teacherPerformance import teacherPerformance
class teacherPerformanceModel:
    def __init__(self):
        pass
    def getAllTeacherPerformance(self):
        performances=[]
        fileList=os.listdir("resources/performanceData")
        for filename in fileList:
            with open("resources/performanceData/"+filename,encoding='utf-8') as f:
                performDict=json.load(f)

                paperTitle, paperAuthor, paperMoneyAmount, paperJournals, paperIF, \
                monographName, monographBelonged, monographMoneyAmount, \
                prizeName, prizeAwardingCompany, prizeWinner, prizeAmount, \
                projectName, projectRequester, projectPrincipal, projectMoneyAmount, \
                performanceID, type, credit, teacherID, lastUpdateTime, performanceHappenTime, relatedPic, note=\
                performDict.get("paperTitle"),performDict.get("paperAuthor"),performDict.get("paperMoneyAmount"),performDict.get("paperJournals"),performDict.get("paperIF"), \
                performDict.get("monographName"),performDict.get("monographBelonged"),performDict.get("monographMoneyAmount"), \
                performDict.get("prizeName"),performDict.get("prizeAwardingCompany"),performDict.get("prizeWinner"),performDict.get("prizeAmount"), \
                performDict.get("projectName"),performDict.get("projectRequester"),performDict.get("projectPrincipal"),performDict.get("projectMoneyAmount"),\
                performDict.get("performanceID"),performDict.get("type"),performDict.get("credit"),performDict.get("teacherID"),performDict.get("lastUpdateTime"),performDict.get("performanceHappenTime"),performDict.get("relatedPic"),performDict.get("note")


                performance=teacherPerformance(paperTitle, paperAuthor, paperMoneyAmount, paperJournals, paperIF, \
                monographName, monographBelonged, monographMoneyAmount, \
                prizeName, prizeAwardingCompany, prizeWinner, prizeAmount, \
                projectName, projectRequester, projectPrincipal, projectMoneyAmount, \
                performanceID, type, credit, teacherID, lastUpdateTime, performanceHappenTime, relatedPic, note)


                performances.append(performance)
        return performances

    def getTeacherPerformanceByID(self,IDlist):
        performances=self.getAllTeacherPerformance()
        selectedPerformance=[]
        for perform in performances:
            if perform.teacherID in IDlist:
                selectedPerform.append(perform)
        return selectedPerformance

    def addTeacherPerformance(self,performance):
        with open("resources/performanceData/" + filename,'w',encoding='utf-8',) as f:
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