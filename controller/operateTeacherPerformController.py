import datetime
import time
import re
#from model.readPerforID import readPerforID
from model.writeToTxt import writeToTxt
from model.teacherPerformanceModel import teacherPerformanceModel
from entity.performanceEntity import teacherPerformance
class operateTeacherPerformController:
    def __init__(self):
        self.tpm=teacherPerformanceModel()


    def getTeacherPerformsByID(self,IDlist):
            return self.tpm.getTeacherPerformance(teacherIDList=IDlist)

