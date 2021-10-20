import datetime
import time
import re
#from model.readPerforID import readPerforID
from model.writeToTxt import writeToTxt
from model.teacherPerformanceModel import teacherPerformanceModel
from entity.performanceEntity import teacherPerformance
class operateTeacherPerform:
    def __init__(self):
        self.tpm=teacherPerformanceModel()

    def getAllTeacherPerforms(self):
        return tpm.readAllTeacherPerformance()

    def getTeacherPerformsByID(self,IDlist):
        if IDlist==[]:
            return self.tpm.getAllTeacherPerformance()
        else:
            return self.tpm.getTeacherPerformanceByID(IDlist)
