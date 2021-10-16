from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt
from controller.operateTeacherInfoController import operateTeacherInfo


class perforDetailWindow:
    def __init__(self,id,j):
        self.ui = QUiLoader().load('resources/ui/perforDetailWindow.ui')
        self.id=id
        self.j=j
        self.ui.perforIDEdit.setText(str(j['performID']))
        self.ui.teacherIDEdit.setText(id)
        self.ui.moneyEdit.setText(str(j['money']))
        self.ui.numEdit.setText(str(j['num']))
        self.ui.sumEdit.setText(str(int(j['money']) * int(j['num'])))
        self.ui.happentimeEdit.setText(j['happenTime'])
        self.ui.updatetimeEdit.setText(j['latestUpdateTime'])
        self.ui.detailInfoEdit.setText(j['detail'])
