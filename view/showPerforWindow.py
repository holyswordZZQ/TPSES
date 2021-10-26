import sys

from PySide6.QtGui import Qt

from view.addPerforWindow import addPerforWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidgetItem, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from controller.operateTeacherPerformController import operateTeacherPerformController
from view.perforDetailWindow import perforDetailWindow
from view.setPerformStartAndEndTimeWindow import setPerformStartAndEndTimeWindow

class showPerforWindow:
    def __init__(self,IDlist):
        self.ui = QUiLoader().load('resources/ui/showPerforInfo.ui')
        self.otpc = operateTeacherPerformController()
        self.IDlist=IDlist   #相应教师信息列表
        self.performList=self.otpc.turnTeacherIdToPerformIdList(self.IDlist)
        self.otpc.getShownPerformances(self.IDlist)
        self.addperforwindow = addPerforWindow()


        if len(self.performList)==0:
            self.showAllInformation(0)
        else:
            self.showAllInformation(1)
        self.ui.table.itemClicked.connect(self.showDetail)
        self.ui.addperforButton.clicked.connect(self.goToAddPer)
        self.ui.returnButton.clicked.connect(self.returnprefer)
        self.ui.refreshButton.clicked.connect(self.refresh)
        self.ui.moneyComboBox.currentIndexChanged.connect(self.refreshTableByConditions)
        self.ui.perforTypeComboBox.currentIndexChanged.connect(self.refreshTableByConditions)
        self.ui.happenTimeComboBox.currentIndexChanged.connect(self.refreshTableByConditions)

        self.perfordetailwindow=None
        self.setperformstartandendtimewindow=None

    def showAllInformation(self,flag):
            self.ui.table.setRowCount(0)
            performances=self.otpc.getTeacherPerformsByID(self.performList,perforID='0')
            if performances==None:
                return
            for performance in performances:
                    rowcount = self.ui.table.rowCount()
                    self.ui.table.insertRow(rowcount)

                    perforID = QTableWidgetItem(performance.performanceID)
                    perforID.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 0, perforID)

                    teacherID = QTableWidgetItem(performance.teacherID)
                    teacherID.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 1, teacherID)

                    workCredit = QTableWidgetItem(performance.credit)
                    workCredit.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 2, workCredit)

                    perforType = QTableWidgetItem(performance.type)
                    perforType.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount, 3, perforType)

                    perforHappenTime=QTableWidgetItem(performance.performanceHappenTime)
                    perforHappenTime.setTextAlignment(Qt.AlignHCenter)
                    self.ui.table.setItem(rowcount,4,perforHappenTime)

    def refreshTableByConditions(self,index=None,periodTime=None):
        moneyText=self.ui.moneyComboBox.currentText()
        if moneyText=='10000以上':
            moneyText='10000-'+str(sys.maxsize)
        elif moneyText=='全部':
            moneyText='0-0'
        perforTypeText=self.ui.perforTypeComboBox.currentText()
        happenTimeText=self.ui.happenTimeComboBox.currentText()
        if periodTime==None:
            if happenTimeText=='自定义时间段':
                self.setperformstartandendtimewindow=setPerformStartAndEndTimeWindow(self.refreshTableByConditions)
                self.setperformstartandendtimewindow.ui.show()
            elif len(happenTimeText)==9:
                str1=happenTimeText.split('-',1)[0]+'0000'
                str2=happenTimeText.split('-',1)[1]+'0000'
                happenTimeText=str1+'-'+str2
                self.performList = self.otpc.getPerformInfoByConditions(moneyText, perforTypeText, happenTimeText)
            elif happenTimeText=='全部':
                self.performList=self.otpc.getPerformInfoByConditions(moneyText, perforTypeText, '0-0')
        else:
            self.ui.happenTimeComboBox.setEditText(periodTime)
            print(periodTime)
            self.performList = self.otpc.getPerformInfoByConditions(moneyText, perforTypeText, periodTime)
            print(self.performList)

        self.showAllInformation(1)
    def showDetail(self):
        listItem=self.ui.table.selectedItems()
        if len(listItem)>1:
            QMessageBox.information(self.ui,"出错啦","一次只能选择一个老师的信息")
        else:
            itemRow=listItem[0].row()
            print(itemRow)
            teacherIdItem=self.ui.table.item(itemRow,1)
            teacherId=teacherIdItem.text()
            perforIdItem=self.ui.table.item(itemRow,0)
            perforId=perforIdItem.text()
            performance=self.otpc.getTeacherPerformsByID(IDlist=[teacherId],perforID=perforId)
            self.perfordetailwindow=perforDetailWindow(performance[0])
            print(performance[0].performanceID)
            self.perfordetailwindow.ui.show()

    def goToAddPer(self):  #业绩信息录入页面
        self.addperforwindow.ui.show()

    def returnprefer(self):  #返回上一级
        self.ui.close()

    def refresh(self):
        self.performList=self.otpc.turnTeacherIdToPerformIdList(self.IDlist)
        self.ui.moneyComboBox.setCurrentText('全部')
        self.ui.perforTypeComboBox.setCurrentText('全部')
        self.ui.happenTimeComboBox.setCurrentText('全部')

        if len(self.performList) == 0:
            self.showAllInformation(0)
        else:
            self.showAllInformation(1)