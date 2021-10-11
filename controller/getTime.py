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

def isIDRight(id):
    reState = re.match('\d\d\d\d\d\d\d\d', id)
    if reState==None:
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