from view.loginWindow import loginWindow
from view.welcomeWindow import welcomeWindow
from view.modifyDetailWindow import modifyDetailWindow
from view.teacherInfoWindow import teacherInfoWindow
from view.modifyInfoWindow import modifyInfoWindow
from view.addInfoWindow import addInfoWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
import os
import PySide6
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
if __name__ == '__main__':
    app=QApplication([])
    e = addInfoWindow()
    d = modifyInfoWindow()
    c = teacherInfoWindow(e, d)
    b = welcomeWindow(c)
    a = loginWindow(b)
    a.ui.show()
    '''mainwindow=QMainWindow()
    mainwindow.setCentralWidget(b.ui)
    mainwindow.centralWidget().getNext()
    mainwindow.setCentralWidget()'''
    app.exec()