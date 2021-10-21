from view.welcomeWindow import welcomeWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
#from controller.getTime import getTime
#from controller.getTime import getPerforID,operateID,isIDRight,addper,getCredit
from controller.operateTeacherInfoController import operateTeacherInfoController
from controller.operateTeacherPerformController import operateTeacherPerformController


class addPerforWindow:
    def __init__(self):
        self.ui = QUiLoader().load('resources/ui/adddetailperWindow.ui')
        self.ui.addButton.clicked.connect(self.add)
        self.ui.cancelButton.clicked.connect(self.cancel)

        self.otpc=operateTeacherPerformController()

    def add(self):
        oTI=operateTeacherInfo()
        perfor_dict={}
        inputId=self.ui.idEdit.text()
        inputTime=self.ui.timeEdit.text()
        state=self.otpc.isIDRight(inputId,inputTime)
        if state==0:
            QMessageBox.warning(self.ui,'出错了','输入的id或发生时间不符合要求')
        elif state==1:
            QMessageBox.warning(self.ui,'出错了','id不存在，请先添加信息')
        elif state==2:
            d = oTI.getTeacherInfoDict(inputId)
            perfor_dict['money']=self.ui.moneyEdit.text()
            perfor_dict['num']=self.ui.numEdit.text()
            perfor_dict['sum']=int(perfor_dict['money'])*int(perfor_dict['num'])
            perfor_dict['happenTime']=self.ui.timeEdit.text()
            perfor_dict['latestUpdateTime']=self.otp.getTime()
            perfor_dict['type']=self.ui.perforBox.currentText()
            perfor_dict['credit']=self.otp.getCredit(perfor_dict['type'])
            perfor_dict['detail']=self.ui.detailInfoEdit.toPlainText()
            perfor_dict['performID']=self.otp.getPerforID()
            id=self.otp.getPerforID()
            self.otp.operateID(id+1)
            d['performance'].append(perfor_dict)
            self.otp.addper(d)
            QMessageBox.information(self.ui,'操作成功','业绩信息已录入')
    def cancel(self):
        self.ui.close()