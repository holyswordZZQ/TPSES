import os

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
        stylesheet=self.ui.styleSheet()
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        print(stylesheet)
        with open('resources/addPerform.css') as file:
            stlst=file.read().format(**os.environ)
            self.ui.setStyleSheet(stylesheet+stlst)
        print(stylesheet)
        self.ui.bgLabel.setProperty('class','bglabel')
        self.ui.perforTypeBox.setCurrentText('论文')  #设置初始的界面，仅仅显示论文的录入
        self.ui.paperWidget.show()
        self.ui.monographWidget.close()
        self.ui.projectWidget.close()
        self.ui.prizeWidget.close()
        self.ui.bookWidget.close()

        self.ui.paperSubmmitButton.clicked.connect(self.add)  #设置添加按钮的点击响应事件
        self.ui.monographSubmmitButton.clicked.connect(self.add)
        self.ui.prizeSubmmitButton.clicked.connect(self.add)
        self.ui.submmitButton.clicked.connect(self.add)
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
        if perforType=='论文' or perforType=='其它':
            self.ui.paperWidget.show()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
            self.ui.bookWidget.close()
        elif perforType=='软著':
            self.ui.paperWidget.close()
            self.ui.monographWidget.show()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
            self.ui.bookWidget.close()
        elif perforType=='项目':
            self.ui.paperWidget.close()
            self.ui.monographWidget.close()
            self.ui.projectWidget.show()
            self.ui.prizeWidget.close()
            self.ui.bookWidget.close()
        elif perforType=='获奖':
            self.ui.paperWidget.close()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.show()
            self.ui.bookWidget.close()
        elif perforType=='出版教材':
            self.ui.paperWidget.close()
            self.ui.monographWidget.close()
            self.ui.projectWidget.close()
            self.ui.prizeWidget.close()
            self.ui.bookWidget.show()



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
        credit=self.ui.creditEdit.text()
        state=self.otpc.isIDOrTimeRight(inputId)
        if state==0:
            QMessageBox.warning(self.ui,'出错了','输入的id或发生时间不符合要求')
            return
        elif state==1:
            QMessageBox.warning(self.ui,'出错了','id不存在，请先添加信息')
            return
        if credit==''or re.match('[0-9]*',credit)==None:
            QMessageBox.warning(self.ui,'出错了','请输入正确的工分!')
            return

        perfor_dict['credit']=self.ui.creditEdit.text()
        perfor_dict['type']=self.ui.perforTypeBox.currentText()
        perfor_dict['teacherID']=self.ui.teacherIDEdit.text()
        perfor_dict['lastUpdateTime']=self.otpc.getCurrentTime()
        perfor_dict['relatedPic']=self.ui.relatedPicEdit.text()
        perfor_dict['note']=self.ui.noteEdit.text()
        perfor_dict['performanceID']=self.otpc.getPerforIDByTxt()
        self.otpc.writePerforIDByTxt(int(perfor_dict['performanceID']) + 1)
        if self.ui.perforTypeBox.currentText() == '论文':
            perfor_dict['paperTitle']=self.ui.paperTitleEdit.text()
            perfor_dict['paperAuthor']=self.ui.paperAuthorEdit.text()
            perfor_dict['paperJournals']=self.ui.paperJournalsEdit.text()
            perfor_dict['paperTime']=self.ui.paperTimeEdit.text()
        elif self.ui.perforTypeBox.currentText()=='软著':
            perfor_dict['monographName']=self.ui.monographNameEdit.text()
            perfor_dict['monographBelonged']=self.ui.monographBelongedEdit.text()
            perfor_dict['monographNumber']=self.ui.monographNumberEdit.text()
            perfor_dict['monographTime']=self.ui.monographTimeEdit.text()
        elif self.ui.perforTypeBox.currentText()=='项目':
            perfor_dict['projectName']=self.ui.projectNameEdit.text()
            perfor_dict['projectSource']=self.ui.projectSourceEdit.text()
            perfor_dict['projectIncharge']=self.ui.projectInchargeEdit.text()
            perfor_dict['projectTime']=self.ui.projectTimeEdit.text()
            perfor_dict['projectApplyerRole']=self.ui.projectApplyerRoleEdit.text()
            perfor_dict['projectType']=self.ui.projectTypeEdit.text()
        elif self.ui.perforTypeBox.currentText()=='获奖':
            perfor_dict['prizeName']=self.ui.prizeNameEdit.text()
            perfor_dict['prizeAwardingCompany']=self.ui.prizeAwardingCompanyEdit.text()
            perfor_dict['prizeProject']=self.ui.prizeProjectEdit.text()
        elif self.ui.perforTypeBox.currentText()=='出版教材':
            perfor_dict['bookName']=self.ui.bookNameEdit.text()
            perfor_dict['bookPublisher']=self.ui.bookPublisherEdit.text()
            perfor_dict['bookISBN']=self.ui.bookISBNEdit.text()
            perfor_dict['bookTime']= self.ui.bookTimeEdit.text()
        self.otpc.addPerform(perfor_dict)
        QMessageBox.information(self.ui,'操作成功','业绩信息已录入')

    def cancel(self):
        self.ui.close()
