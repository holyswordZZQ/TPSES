from model.writeTeacherInfo import writeTeacherInfo
from model.readAllTeacherInfo import readALLTeacherInfo

def showUnchangedInfo():
    lst=readALLTeacherInfo()
    return lst

def modifyTeacherInfo(dict):

    writeTeacherInfo(dict)

