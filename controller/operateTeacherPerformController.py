import datetime
import time
import re
#from model.readPerforID import readPerforID
from model.writeToTxt import writeToTxt


from model.teacherInfoModel import teacherInfoModel

class operateTeacherPer:
    def __init__(self):
        self.tim=teacherInfoModel()
    def getTime(self):
        today=datetime.date.today()
        return str(today.year)+str(today.month)+str(today.day)

    def getPerforID(self):
        return self.tim.readPerforID()

    def operateID(self,id):
        writeToTxt(id)

    def isIDRight(self,id,time):
        reState = re.match('\d\d\d\d\d\d\d\d', id)
        reTimeState=re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])',time)
        if reState==None or reTimeState==None:
            state=0
        else:
            if id+'.json' not in self.tim.readAllTeacherID():
                state=1
            else:
                state=2
        return state

    def addper(self,d):
        self.tim.writeTeacherInfo(d)

    def getCredit(self,perforType):
        dict=self.tim.readPerforAndCredit()
        return dict[perforType]