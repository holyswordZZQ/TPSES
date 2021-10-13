from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt, QPalette, QBrush, QPixmap


class welcomeWindow():  # 欢迎登录界面
    def __init__(self,teacherInfoWindow):
        self.teacherInfoWindow=teacherInfoWindow
        qfile_stats = QFile("resources/ui/welcome.ui")
        self.ui = QUiLoader().load(qfile_stats)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("resources/images/welcomeWindow.jpg")))
        self.ui.setPalette(palette)
        self.ui.getintoButton.clicked.connect(self.getNext)
        self.ui.close()

    def getNext(self):  #到达下一个页面，即功能页面
        self.ui.close()
        
