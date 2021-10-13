import datetime
import time
import re
from model.readPerforID import readPerforID
from model.writeToTxt import writeToTxt
from model.readAllTeacherInfo import readAllTeacherID
from model.writeTeacherInfo import writeTeacherInfo
from model.readPerforAndCredit import readPerforAndCredit

def getTime():
    today=datetime.date.today()
    return str(today.year)+str(today.month)+str(today.day)

def getPerforID():
    return readPerforID()

def operateID(id):
    writeToTxt(id)

def isIDRight(id,time):
    reState = re.match('\d\d\d\d\d\d\d\d', id)
    reTimeState=re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])',time)
    if reState==None or reTimeState==None:
        state=0
    else:
        if id+'.json' not in readAllTeacherID():
            state=1
        else:
            state=2
    return state

def addper(d):
    writeTeacherInfo(d)

def getCredit(perforType):
    dict=readPerforAndCredit()
    return dict[perforType]