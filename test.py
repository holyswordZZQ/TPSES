import time

from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from view.welcomeWindow import welcomeWindow
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QApplication
from view.teacherInfoWindow import teacherInfoWindow
from view.loginWindow import loginWindow



app=QApplication([])
mw=QMainWindow()
ww=welcomeWindow(None)
lgw=loginWindow(mw)

tiw=teacherInfoWindow(None,None)
mw.setGeometry(0,0,1920,1000)
mw.setCentralWidget(ww.ui)
if mw.centralWidget()==ww.ui:
    mw.centralWidget().getintoButton.clicked.connect(lambda :mw.setCentralWidget(tiw.ui))
#test for github
lgw.ui.show()



app.exec_()