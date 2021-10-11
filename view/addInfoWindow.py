from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt
from controller.addTeacherInfo import addTeacherInfo,getExistedTeacher

import re
import os

class addInfoWindow:   #信息增添窗口
    def __init__(self):
        qfile_stats = QFile('resources/ui/addWindow.ui')
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.submitButton.clicked.connect(self.submit)  #提交按钮
        self.ui.cancelButton.clicked.connect(self.returnToJieMian2)  #返回上一级按钮

    def submit(self):
        textID = self.ui.idEdit.text()
        textName=self.ui.nameEdit.text()
        reState = re.match('\d\d\d\d\d\d\d\d', textID)  #正则表达式，要求输入的id符合8位数字
        fileName = textID + '.json'  #得到文件名
        if getExistedTeacher(fileName):
            QMessageBox.warning(self.ui, '出错了', 'id已存在')
        else:  #相反则表明输入的id在所有文件中不存在，可以进行添加操作
            if reState != None and textName != '': #输入均符合要求且姓名不为空
                d = {}
                d['id'] = self.ui.idEdit.text()
                d['name'] = self.ui.nameEdit.text()
                d['college'] = self.ui.collegeBox.currentText()
                d['title'] = self.ui.titleBox.currentText()
                d['performance'] = ''
                d['time'] = self.ui.timeEdit.text()
                addTeacherInfo(d)
                QMessageBox.information(self.ui, '操作成功', '信息已录入')
            elif reState == None:
                QMessageBox.warning(self.ui, '操作错误', '工号输入有误')
            elif textName == '':
                QMessageBox.warning(self.ui, '操作错误', '姓名不能为空')

    def returnToJieMian2(self):
        self.ui.close()