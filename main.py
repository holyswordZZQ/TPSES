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
from  qt_material import  apply_stylesheet

app=QApplication([])
#apply_stylesheet(app,theme='light_blue.xml')

mw=QMainWindow()
tiw=teacherInfoWindow()
ww=welcomeWindow(tiw)
lgw=loginWindow(mw)

mw.setGeometry(270,65,810,640)
mw.setFixedSize(mw.width(),mw.height())
mw.setCentralWidget(ww.ui)


if mw.centralWidget()==ww.ui:
    mw.centralWidget().getintoButton.clicked.connect(lambda :mw.setCentralWidget(tiw.ui))
lgw.ui.show()
app.exec()