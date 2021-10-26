from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import Qt
from entity.performanceEntity import teacherPerformance

class perforDetailWindow:
    def __init__(self,performance):
        self.ui = QUiLoader().load('resources/ui/showPerforDetailWindow.ui')
        self.ui.stackedWidget.setCurrentIndex(1)
        perforType=performance.type
        if perforType=='论文':
            self.ui.paperWidget.show()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
            self.ui.paperTitleEdit_2.setText(performance.paperTitle)
            self.ui.paperAuthorEdit.setText(performance.paperAuthor)
            self.ui.paperJournalsEdit.setText(performance.paperJournals)
            self.ui.paperMoneyAmountEdit_2.setText(performance.paperMoneyAmount)
            self.ui.paperIFEdit_2.setText(performance.paperIF)
        elif perforType=='软著':
            self.ui.paperWidget.close()
            self.ui.monographWidget.show()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
            self.ui.monographNameEdit_2.setText(performance.monographName)
            self.ui.monographAuthorEdit.setText(performance.monographBelonged)
            self.ui.monographMoneyAmountEdit_2.setText(performance.monographMoneyAmount)
        elif perforType=='项目':
            self.ui.paperWidget.close()
            self.ui.monographWidget.close()
            self.ui.projectWidget.show()
            self.ui.prizeWidget.close()
            self.ui.projectNameEdit_2.setText(performance.projectName)
            self.ui.projectRequesterEdit_2.setText(performance.projectRequester)
            self.ui.projectPrincipalEdit_2.setText(performance.projectPrincipal)
            self.ui.projectMoneyAmountEdit_2.setText(performance.projectMoneyAmount)
        elif perforType=='获奖':
            self.ui.paperWidget.close()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.show()
            self.ui.prizeNameEdit_5.setText(performance.prizeName)
            self.ui.prizeAwardingCompanyEdit_5.setText(performance.prizeAwardingCompany)
            self.ui.prizeWinnerEdit_5.setText(performance.prizeWinner)
            self.ui.prizeMoneyAmountEdit_5.setText(performance.prizeAmount)
        else:
            self.ui.paperWidget.show()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
        self.ui.teacherIDEdit.setText(performance.teacherID)
        self.ui.perforTypeEdit.setText(performance.type)
        self.ui.happenTimeEdit.setText(performance.performanceHappenTime)
        self.ui.noteEdit.setText(performance.note)
        self.ui.creditEdit.setText(performance.credit)

        self.ui.nextPageButton.clicked.connect(self.goToNextPage)
        self.ui.preferPageButton.clicked.connect(self.goToPreferPage)

    def goToNextPage(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def goToPreferPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

