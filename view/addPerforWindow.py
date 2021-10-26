from view.welcomeWindow import welcomeWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
#from controller.getTime import getTime
#from controller.getTime import getPerforID,operateID,isIDRight,addper,getCredit
from controller.operateTeacherInfoController import operateTeacherInfoController
from controller.operateTeacherPerformController import operateTeacherPerformController


class addPerforWindow:
    def __init__(self):
        self.ui = QUiLoader().load('resources/ui/addPerforWindow.ui')

        self.ui.perforTypeBox.setCurrentText('论文')  #设置初始的界面，仅仅显示论文的录入
        self.ui.paperWidget.show()
        self.ui.monographWidget.close()
        self.ui.projectWidget.close()
        self.ui.prizeWidget.close()

        self.ui.paperSubmmitButton.clicked.connect(self.add)  #设置添加按钮的点击响应事件
        self.ui.monographSubmmitButton.clicked.connect(self.add)
        self.ui.prizeSubmmitButton.clicked.connect(self.add)
        self.ui.projectSubmmitButton.clicked.connect(self.add)

        self.ui.paperCancelButton.clicked.connect(self.cancel)  #设置取消按钮的点击响应事件
        self.ui.monographCancelButton.clicked.connect(self.cancel)
        self.ui.prizeCancelButton.clicked.connect(self.cancel)
        self.ui.projectCancelButton.clicked.connect(self.cancel)

        self.ui.perforTypeBox.currentTextChanged.connect(self.modifyUi)  #根据业绩类型，生成不同的ui界面
        self.ui.openFileButton.clicked.connect(self.openFile)

        self.otpc=operateTeacherPerformController()

    def modifyUi(self):
        perforType=self.ui.perforTypeBox.currentText()   #根据下拉框中的选项动态设置相应ui
        if perforType=='论文':
            self.ui.paperWidget.show()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
        elif perforType=='软著':
            self.ui.paperWidget.close()
            self.ui.monographWidget.show()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
        elif perforType=='项目':
            self.ui.paperWidget.close()
            self.ui.monographWidget.close()
            self.ui.projectWidget.show()
            self.ui.prizeWidget.close()
        elif perforType=='获奖':
            self.ui.paperWidget.close()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.show()

    def openFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)  # 设置文件过滤器，这里是任何文件，包括目录
        dialog.setViewMode(QFileDialog.Detail)  # 设置显示文件的模式，这里是详细模式
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.ui.relatedPicEdit.setText(fileNames[0])

    def add(self):
        perfor_dict={}
        inputId=self.ui.teacherIDEdit.text()
        inputTime=self.ui.happenTimeEdit.text()
        state=self.otpc.isIDOrTimeRight(inputId,inputTime)
        if state==0:
            QMessageBox.warning(self.ui,'出错了','输入的id或发生时间不符合要求')
        elif state==1:
            QMessageBox.warning(self.ui,'出错了','id不存在，请先添加信息')
        elif state==2:
            perfor_dict['credit']=self.ui.creditEdit.text()
            perfor_dict['type']=self.ui.perforTypeBox.currentText()
            perfor_dict['teacherID']=self.ui.teacherIDEdit.text()
            perfor_dict['performanceHappenTime']=self.ui.happenTimeEdit.text()
            perfor_dict['lastUpdateTime']=self.otpc.getCurrentTime()
            perfor_dict['relatedPic']=self.ui.relatedPicEdit.text()
            perfor_dict['note']=self.ui.noteEdit.text()
            perfor_dict['performanceID']=self.otpc.getPerforIDByTxt()
            self.otpc.writePerforIDByTxt(int(perfor_dict['performanceID']) + 1)
            if self.ui.perforTypeBox.currentText() == '论文':
                perfor_dict['paperTitle']=self.ui.paperTitleEdit.text()
                perfor_dict['paperAuthor']=self.ui.paperWriterEdit.text()
                perfor_dict['paperMoneyAmount']=self.ui.paperMoneyAmountEdit.text()
                perfor_dict['paperJournals']=self.ui.paperJournalEdit.text()
                perfor_dict['paperIF']=self.ui.paperIFEdit.text()
            elif self.ui.perforTypeBox.currentText()=='软著':
                perfor_dict['monographName']=self.ui.monographNameEdit.text()
                perfor_dict['monographBelonged']=self.ui.monographWriterEdit.text()
                perfor_dict['monographMoneyAmount']=self.ui.monographMoneyAmountEdit.text()
            elif self.ui.perforTypeBox.currentText()=='项目':
                perfor_dict['projectName']=self.ui.projectNameEdit.text()
                perfor_dict['projectRequester']=self.ui.projectRequesterEdit.text()
                perfor_dict['projectPrincipal']=self.ui.projectPrincipalEdit.text()
                perfor_dict['projectMoneyAmount']=self.ui.projectMoneyAmountEdit.text()
            elif self.ui.perforTypeBox.currentText()=='获奖':
                perfor_dict['prizeName']=self.ui.prizeNameEdit.text()
                perfor_dict['prizeAwardingCompany']=self.ui.prizeAwardingCompanyEdit.text()
                perfor_dict['prizeWinner']=self.ui.prizeWinnerEdit.text()
                perfor_dict['prizeAmount']=self.ui.prizeMoneyAmountEdit.text()

            self.otpc.addPerform(perfor_dict)
            QMessageBox.information(self.ui,'操作成功','业绩信息已录入')

    def cancel(self):
        self.ui.close()
