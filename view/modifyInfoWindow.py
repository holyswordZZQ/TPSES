from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt
from controller.addTeacherInfo import getExistedTeacher
import re
from view.modifyDetailWindow import modifyDetailWindow

class modifyInfoWindow():
    modifyDetailWindow=None
    def __init__(self):
        qfile_stats = QFile('resources/ui/modifyInformationWindow.ui')
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.ensureButton.clicked.connect(self.modify)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def modify(self):
        textID = self.ui.idEdit.text()
        print('text:'+textID)
        m = re.match('\d\d\d\d\d\d\d\d', textID)  # 正则表达式判断输入的id是否规范
        if m == None:
            QMessageBox.warning(self.ui, '输入错误', '输入的id不符合要求')
        else:
            if not getExistedTeacher(textID+'.json'):
                QMessageBox.warning(self.ui, '出错了', 'id不存在，请先添加信息')
            else:
                self.modifyDetailWindow=modifyDetailWindow(textID)
                self.modifyDetailWindow.ui.show()
                self.ui.close()

    def cancel(self):
        self.ui.close()
