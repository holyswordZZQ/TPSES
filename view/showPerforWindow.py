from PySide6.QtGui import Qt

from TPSES.view.addPerforWindow import addPerforWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidgetItem, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from TPSES.controller.operateTeacherPerformController import operateTeacherPerformController
from TPSES.view.perforDetailWindow import perforDetailWindow

class showPerforWindow:
    def __init__(self,IDlist):
        self.ui = QUiLoader().load('resources/ui/showPerforInfo.ui')
        self.IDlist=IDlist
        self.addperforwindow = addPerforWindow()

        self.otpc=operateTeacherPerformController()

        self.showAllInformation()
        self.ui.table.itemClicked.connect(self.showDetail)
        self.ui.addperforButton.clicked.connect(self.goToAddPer)
        self.ui.returnButton.clicked.connect(self.returnprefer)
        self.perfordetailwindow=None

    def showAllInformation(self):
            self.ui.table.setRowCount(0)
            performances=self.otpc.getTeacherPerformsByID(self.IDlist)
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


    def showDetail(self):
        listItem=self.ui.table.selectedItems()

        if len(listItem)>1:
            QMessageBox.information(self.ui,"出错啦","一次只能选择一个老师的信息")
        else:
            itemRow=listItem[0].row()
            teacherIdItem=self.ui.table.item(itemRow,1)
            teacherId=teacherIdItem.text()
            performance=self.otpc.getTeacherPerformsByID(IDlist=[teacherId])
            self.perfordetailwindow=perforDetailWindow(performance)
            self.perfordetailwindow.ui.show()

    def goToAddPer(self):  #业绩信息录入页面
        self.addperforwindow.ui.show()
    def returnprefer(self):
        self.ui.close()