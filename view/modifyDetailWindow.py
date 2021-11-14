import os

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt, QPixmap
from controller.operateTeacherInfoController import operateTeacherInfoController
from qt_material import apply_stylesheet
import re

class modifyDetailWindow:
    def __init__(self,textID,data):
        print(data)
        print(textID)
        self.ot=operateTeacherInfoController()
        self.textID = textID
        self.data=data
        qfile_stats = QFile('resources/ui/modifyTeacherDetaiInfolWindow.ui')
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        apply_stylesheet(self.ui,theme='light_blue.xml',invert_secondary=True)
        stylesheet = self.ui.styleSheet()
        with open('resources/addTeacherInfo.css') as file:
            styleStr=file.read().format(**os.environ)

        for teacher in self.data:
            if teacher.id==self.textID:
                self.ui.nameEdit.setText(teacher.name)
                self.ui.timeEdit.setText(teacher.time)
        self.ui.nameEdit.setStyleSheet(styleStr)
        self.ui.timeEdit.setStyleSheet(styleStr)
        self.ui.titleBox.setStyleSheet(styleStr)
        self.ui.collegeBox.setStyleSheet(styleStr)
        self.ui.label_7.setStyleSheet(styleStr)
        self.ui.label3.setStyleSheet(styleStr)
        self.ui.ensureButton.clicked.connect(self.change)
        self.ui.cancelButton.clicked.connect(self.cancel)

        self.image=QPixmap()
        self.image.load('resources/images/2.jpg')
        self.ui.bgLabel.setPixmap(self.image)

    def change(self):
        reTimeState=re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])',self.ui.timeEdit.text())
        if reTimeState!=None:
            dict = {}
            dict['id']=self.textID
            dict['name'] = self.ui.nameEdit.text()
            dict['college'] = self.ui.collegeBox.currentText()
            dict['title'] = self.ui.titleBox.currentText()
            dict['time'] = self.ui.timeEdit.text()
            dict['available']='1'
            self.ot.modifyTeacherInfo(dict)
            QMessageBox.information(self.ui, '操作成功', '信息修改成功')
        else:
            QMessageBox.warning(self.ui,'操作失败','输入的时间不符合要求')

    def cancel(self):  #取消，即返回上一级
        self.ui.close()
