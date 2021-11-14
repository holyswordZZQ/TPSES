from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt, QPixmap
from controller.operateTeacherInfoController import operateTeacherInfoController
from qt_material import apply_stylesheet
import re
import os

class addInfoWindow:   #信息增添窗口
    def __init__(self):
        self.otic=operateTeacherInfoController()
        self.ui = QUiLoader().load('resources/ui/addTeacherInfoWindow.ui')
        apply_stylesheet(self.ui,'light_blue.xml',invert_secondary=True)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        with open('resources/addTeacherInfo.css') as file:
            styleStr=file.read().format(**os.environ)

           # self.ui.setStyleSheet(stylesheet+file.read().format(**os.environ))
        self.ui.idEdit.setStyleSheet(styleStr)  #设置每个控件的样式
        self.ui.nameEdit.setStyleSheet(styleStr)
        self.ui.timeEdit.setStyleSheet(styleStr)
        self.ui.titleBox.setStyleSheet(styleStr)
        self.ui.collegeBox.setStyleSheet(styleStr)
        self.ui.label1.setStyleSheet(styleStr)
        self.ui.label_7.setStyleSheet(styleStr)
        self.ui.label3.setStyleSheet(styleStr)
        #print(self.ui.styleSheet())
        self.ui.submitButton.clicked.connect(self.submit)  #提交按钮
        self.ui.cancelButton.clicked.connect(self.returnToJieMian2)  #返回上一级按钮

        self.image = QPixmap()
        self.image.load('resources/images/2.jpg')
        self.ui.bgLabel.setPixmap(self.image)

    def submit(self):
        textID = self.ui.idEdit.text()
        textName=self.ui.nameEdit.text()
        textTime=self.ui.timeEdit.text()
        reState = re.match('\d\d\d\d\d\d\d\d', textID)  #正则表达式，要求输入的id符合8位数字
        reTimeState=re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])',textTime)
        if self.otic.getSingleTeacherInfo(textID)!=-1:
            QMessageBox.warning(self.ui, '出错了', 'id已存在')
        else:  #相反则表明输入的id在所有文件中不存在，可以进行添加操作
            if reState != None and textName != '' and reTimeState!=None: #输入均符合要求且姓名不为空
                d = {}
                d['id'] = self.ui.idEdit.text()
                d['name'] = self.ui.nameEdit.text()
                d['college'] = self.ui.collegeBox.currentText()
                d['title'] = self.ui.titleBox.currentText()
                d['time'] = self.ui.timeEdit.text()
                d['available']='1'
                self.otic.addTeacherInfo(d)
                QMessageBox.information(self.ui, '操作成功', '信息已录入')
            elif reState == None:
                QMessageBox.warning(self.ui, '操作错误', '工号输入有误')
            elif textName == '':
                QMessageBox.warning(self.ui, '操作错误', '姓名不能为空')
            elif reTimeState==None:
                QMessageBox.warning(self.ui, '操作错误', '时间输入不符合要求')

    def returnToJieMian2(self):
        self.ui.close()