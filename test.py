import time

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from view.welcomeWindow import welcomeWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from view.teacherInfoWindow import teacherInfoWindow
from view.loginWindow import loginWindow
from view.addInfoWindow import addInfoWindow
from view.modifyInfoWindow import modifyInfoWindow
from view.addPerforWindow import addPerforWindow


app=QApplication([])
mw=QMainWindow()
aIW=addInfoWindow()
mIW=modifyInfoWindow()
aPW=addPerforWindow()
tiw=teacherInfoWindow(aIW,mIW)
ww=welcomeWindow(tiw)
lgw=loginWindow(mw)

mw.setGeometry(0,0,850,1000)
mw.setCentralWidget(ww.ui)
if mw.centralWidget()==ww.ui:
    mw.centralWidget().getintoButton.clicked.connect(lambda :mw.setCentralWidget(tiw.ui))

lgw.ui.show()



app.exec()