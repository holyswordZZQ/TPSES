from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize
from PySide6.QtGui import Qt, QPixmap, QPicture,QIcon

class setPerformStartAndEndTimeWindow:
    def __init__(self,refreshTableFunc):
        self.ui=QUiLoader().load('resources/ui/setPerformStartAndEndTimeWindow.ui')
        self.refreshTableFunc=refreshTableFunc
        self.ui.ensureButton.clicked.connect(self.refresh)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def refresh(self):
        self.startDate = str(self.ui.startDateEdit.date().year()) + self.modifyString(str(self.ui.startDateEdit.date().month())) + self.modifyString(str(self.ui.startDateEdit.date().day()))
        self.endDate = str(self.ui.endDateEdit.date().year()) + self.modifyString(str(self.ui.endDateEdit.date().month())) + self.modifyString(str(self.ui.endDateEdit.date().day()))
        self.refreshTableFunc(periodTime=self.startDate+'-'+self.endDate)
        self.ui.close()

    def modifyString(self,str):
        if len(str)==1:
            return '0'+str
        else:
            return str

    def cancel(self):
        self.startDate='全部'
        self.endDate=''
        self.ui.close()