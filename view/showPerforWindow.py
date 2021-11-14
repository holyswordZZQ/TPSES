import os
import sys

from PySide6.QtGui import Qt, QPixmap
from qt_material import apply_stylesheet

from view.addPerforWindow import addPerforWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidgetItem, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from controller.operateTeacherPerformController import operateTeacherPerformController
from view.perforDetailWindow import perforDetailWindow
from view.setPerformStartAndEndTimeWindow import setPerformStartAndEndTimeWindow
from view.exportPerformFileWindow import exportPerformFileWindow
extra={
    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',

    # Font
    'font-family': 'Roboto',
}
class showPerforWindow:
    def __init__(self,IDlist):
        self.ui = QUiLoader().load('resources/ui/showPerforInfo.ui')
        apply_stylesheet(self.ui, 'light_blue.xml', invert_secondary=True,extra=extra)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        with open('resources/showPerform.css') as file:
            styleStr = file.read().format(**os.environ)
        self.ui.setGeometry(270,65,810,635)
        self.ui.divideLabel.setStyleSheet(styleStr)
        self.ui.table.setStyleSheet(styleStr)
        self.image = QPixmap()
        self.image.load('resources/images/yun.png')
        self.ui.imageLabel.setPixmap(self.image)
        self.otpc = operateTeacherPerformController()
        self.IDlist=IDlist   #相应教师信息列表
        self.performList=self.otpc.turnTeacherIdToPerformIdList(self.IDlist)  #本窗口维护一个教师履历ID的列表，根据它的内容改变表格中显示的业绩
        self.otpc.getShownPerformances(self.IDlist)  #设置controller层shownPerformances的初值
        self.addperforwindow = addPerforWindow()

        self.showAllInformation()
        self.ui.table.itemClicked.connect(self.showDetail)
        self.ui.addperforButton.clicked.connect(self.goToAddPerform)
        self.ui.returnButton.clicked.connect(self.returnprefer)
        self.ui.refreshButton.clicked.connect(self.refresh)
        self.ui.moneyComboBox.currentIndexChanged.connect(self.refreshTableByConditions)  #三个筛选框
        self.ui.perforTypeComboBox.currentIndexChanged.connect(self.refreshTableByConditions)
        self.ui.happenTimeComboBox.currentIndexChanged.connect(self.refreshTableByConditions)
        self.ui.exportButton.clicked.connect(self.exportPerform)
        self.ui.addperforButton.setProperty('class','danger')
        self.ui.returnButton.setProperty('class','warning')
        self.ui.exportButton.setProperty('class','success')

        self.perfordetailwindow=None
        self.setperformstartandendtimewindow=None
        self.exportperformfilewindow=None

    def showAllInformation(self):
            self.ui.table.setRowCount(0)
            performances=self.otpc.getTeacherPerformsByID(self.performList,perforID='0')  #根据业绩ID列表返回一个业绩对象列表
            if performances==None:
                return
            for performance in performances:   #表格中显示信息
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

    def refreshTableByConditions(self,index=None,periodTime=None):  #根据三个筛选框的条件来改变表格中的内容
        moneyText=self.ui.moneyComboBox.currentText()
        if moneyText=='10000以上':  #将金额超过1w的业绩设置为10000——最大
            moneyText='10000-'+str(sys.maxsize)
        elif moneyText=='全部':  #金额筛选条件为全部时，设置为'0-0'以方便后续的比较操作
            moneyText='0-0'
        perforTypeText=self.ui.perforTypeComboBox.currentText()
        happenTimeText=self.ui.happenTimeComboBox.currentText()
        if periodTime==None:
            if happenTimeText=='自定义时间段':
                self.setperformstartandendtimewindow=setPerformStartAndEndTimeWindow(self.refreshTableByConditions)   #显示设置自定义时间的窗口
                self.setperformstartandendtimewindow.ui.show()
            elif len(happenTimeText)==9:
                str1=happenTimeText.split('-',1)[0]+'0000'
                str2=happenTimeText.split('-',1)[1]+'0000'
                happenTimeText=str1+'-'+str2
                self.performList = self.otpc.getPerformInfoByConditions(moneyText, perforTypeText, happenTimeText)    #返回符合三者条件的业绩ID列表
            elif happenTimeText=='全部':
                self.performList=self.otpc.getPerformInfoByConditions(moneyText, perforTypeText, '0-0')
        else:
            self.ui.happenTimeComboBox.setEditText(periodTime)
            self.performList = self.otpc.getPerformInfoByConditions(moneyText, perforTypeText, periodTime)

        self.showAllInformation()
    def showDetail(self):
        listItem=self.ui.table.selectedItems()
        if len(listItem)>1:
            QMessageBox.information(self.ui,"出错啦","一次只能选择一个老师的信息")
        else:
            itemRow=listItem[0].row()
            print(itemRow)
            teacherIdItem=self.ui.table.item(itemRow,1)   #得到选中行的教师ID以及业绩ID
            teacherId=teacherIdItem.text()
            perforIdItem=self.ui.table.item(itemRow,0)
            perforId=perforIdItem.text()
            performance=self.otpc.getTeacherPerformsByID(IDlist=[teacherId],perforID=perforId)  #返回所选中的业绩对象
            self.perfordetailwindow=perforDetailWindow(performance[0])
            print(performance[0].performanceID)
            self.perfordetailwindow.ui.show()

    def goToAddPerform(self):  #业绩信息录入页面
        self.addperforwindow.ui.show()

    def returnprefer(self):  #返回上一级
        self.ui.close()

    def refresh(self):
        self.performList=self.otpc.turnTeacherIdToPerformIdList(self.IDlist)
        self.ui.moneyComboBox.setCurrentText('全部')
        self.ui.perforTypeComboBox.setCurrentText('全部')
        self.ui.happenTimeComboBox.setCurrentText('全部')
        self.showAllInformation()

    def exportPerform(self):
        self.exportperformfilewindow=exportPerformFileWindow(self.performList)
        self.exportperformfilewindow.ui.show()

