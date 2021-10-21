import datetime
import time
import re
#from model.readPerforID import readPerforID
from TPSES.model.writeToTxt import writeToTxt
from TPSES.model.teacherPerformanceModel import teacherPerformanceModel
from TPSES.entity.performanceEntity import teacherPerformance
class operateTeacherPerformController:
    def __init__(self):
        self.tpm=teacherPerformanceModel()


    def getTeacherPerformsByID(self,IDlist):
            return self.tpm.getTeacherPerformance(teacherIDList=IDlist)

