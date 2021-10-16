from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt
from controller.operateTeacherInfoController import operateTeacherInfo
import re

class modifyDetailWindow:
    def __init__(self,textID,data):
        print(data)
        print(textID)
        self.ot=operateTeacherInfo()
        self.textID = textID
        self.data=data
        qfile_stats = QFile('resources/ui/modifyDetailWindow.ui')
        self.ui = QUiLoader().load(qfile_stats)


        for item in self.data:
            if item[0]==self.textID:
                self.ui.nameEdit.setText(item[1])
                self.ui.timeEdit.setText(item[5])
                self.performance=item[4]
                print

        self.ui.ensureButton.clicked.connect(self.change)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def change(self):
        reTimeState=re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])',self.ui.timeEdit.text())
        if reTimeState!=None:
            dict = {}
            dict['id']=self.textID
            dict['name'] = self.ui.nameEdit.text()
            dict['college'] = self.ui.collegeEdit.currentText()
            dict['title'] = self.ui.titleEdit.currentText()
            dict['time'] = self.ui.timeEdit.text()
            dict['performance']=self.performance
            dict['available']='1'
            self.ot.modifyTeacherInfo(dict)
            QMessageBox.information(self.ui, '操作成功', '信息修改成功')
        else:
            QMessageBox.warning(self.ui,'操作失败','输入的时间不符合要求')

    def cancel(self):  #取消，即返回上一级
        self.ui.close()
