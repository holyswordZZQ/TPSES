from model.writeTeacherInfo import writeTeacherInfo
from model.readAllTeacherInfo import readAllTeacherID

#from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem

import re
import os
def addTeacherInfo(d):

    writeTeacherInfo(d)

def getExistedTeacher(id):
    list=readAllTeacherID()
    return id in list

