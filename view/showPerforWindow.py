from PySide6.QtGui import Qt

from view.addPerforWindow import addPerforWindow
from view.welcomeWindow import welcomeWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidgetItem, QTableWidgetItem
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from controller.operateTeacherInfoController import operateTeacherInfo
from view.perforDetailWindow import perforDetailWindow

class showPerforWindow:
    def __init__(self,list):
        self.ui = QUiLoader().load('resources/ui/showPerforInfo.ui')
        self.list=list
        self.addperforwindow = addPerforWindow()
        self.oTI=operateTeacherInfo()
        self.showAllInformation()
        self.ui.table.itemClicked.connect(self.showDetail)
        self.ui.addperforButton.clicked.connect(self.goToAddPer)
        self.ui.returnButton.clicked.connect(self.returnprefer)
        self.perfordetailwindow=None

    def showAllInformation(self):
        if len(self.list)==0:
            self.ui.table.setRowCount(0)
            teacherList=self.oTI.getTeacherIDList()
            for item in teacherList:
                dict = self.oTI.getTeacherInfoDict(item)
                perforList = dict['performance']
                for i in range(len(perforList)):
                    rowcount = self.ui.table.rowCount()
                    self.ui.table.insertRow(rowcount)
                    perforID = QTableWidgetItem(str(perforList[i]["performID"]))
                    perforID.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 0, perforID)

                    teacherID = QTableWidgetItem(item)
                    teacherID.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 1, teacherID)

                    workCredit = QTableWidgetItem(str(perforList[i]["credit"]))
                    workCredit.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 2, workCredit)

                    perforType = QTableWidgetItem(perforList[i]['type'])
                    perforType.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 3, perforType)

        else:
            self.ui.table.setRowCount(0)
            for item in self.list:
                dict=self.oTI.getTeacherInfoDict(item)
                perforList=dict['performance']
                for i in range(len(perforList)):
                    rowcount=self.ui.table.rowCount()
                    self.ui.table.insertRow(rowcount)
                    perforID=QTableWidgetItem(str(perforList[i]["performID"]))
                    perforID.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount,0,perforID)

                    teacherID=QTableWidgetItem(item)
                    teacherID.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount,1,teacherID)

                    workCredit=QTableWidgetItem(str(perforList[i]["credit"]))
                    workCredit.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount,2,workCredit)

                    perforType=QTableWidgetItem(perforList[i]['type'])
                    perforType.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount,3,perforType)

    def showDetail(self):
        listItem=self.ui.table.selectedItems()
        for i in listItem:
            a=i.row()
            perforIdItem=self.ui.table.item(a,0)
            teacherIdItem=self.ui.table.item(a,1)
        b=teacherIdItem.text()
        dict=self.oTI.getTeacherInfoDict(b)
        list=dict['performance']
        for j in list:
            if j['performID']==int(perforIdItem.text()):

                self.perfordetailwindow=perforDetailWindow(b,j)
                self.perfordetailwindow.ui.show()

    def goToAddPer(self):  #业绩信息录入页面
        self.addperforwindow.ui.show()
    def returnprefer(self):
        self.ui.close()