from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import Qt
from controller.addTeacherInfo import getExistedTeacher
from controller.modifyTeacherInfo import showUnchangedInfo,modifyTeacherInfo
from controller.operateTeacherInfo import operateTeacherInfo
import re

class modifyDetailWindow:

    def __init__(self,textID):
        self.textID = textID
        qfile_stats = QFile('resources/ui/modifyDetailWindow.ui')
        oTI=operateTeacherInfo()
        self.ui = QUiLoader().load(qfile_stats)
        lst=oTI.getTeacherInfo()
        print(lst)
        for item in lst:
            if item[0]==self.textID:
                print(item)
                self.ui.nameEdit.setText(item[1])
                self.ui.timeEdit.setText(item[5])

        self.ui.ensureButton.clicked.connect(self.change)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def change(self):
        dict = {}
        dict['id']=self.textID
        dict['name'] = self.ui.nameEdit.text()
        dict['college'] = self.ui.collegeEdit.currentText()
        dict['title'] = self.ui.titleEdit.currentText()
        dict['time'] = self.ui.timeEdit.text()
        modifyTeacherInfo(dict)
        QMessageBox.information(self.ui, '操作成功', '信息修改成功')

    def cancel(self):  #取消，即返回上一级

        self.ui.close()
        del self
