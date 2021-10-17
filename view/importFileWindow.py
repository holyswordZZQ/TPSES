from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem, \
    QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize
from PySide6.QtGui import Qt, QPixmap, QPicture,QIcon
from controller.operateTeacherInfoByExcelController import operateTeacherInfoByExcelController

class importFileWindow:
    def __init__(self):
        self.ui = QUiLoader().load('resources/ui/importFileDialog.ui')

        self.otibe=operateTeacherInfoByExcelController()

        self.ui.openFileButton.clicked.connect(self.openFile)
        self.ui.importInfoButton.clicked.connect(self.submitTeacherInfo)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def openFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)# 设置文件过滤器，这里是任何文件，包括目录
        dialog.setViewMode(QFileDialog.Detail)# 设置显示文件的模式，这里是详细模式
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.ui.fileNameEdit.setText(fileNames[0])

    def submitTeacherInfo(self):
        try:
            filename=self.ui.fileNameEdit.text()
            if filename!='':
                if '.xlsx' not in filename and '.xls' not in filename:
                    QMessageBox.warning(self.ui,'出错了','上传的不是excel文件')
                else:
                    repeatedTeacherIDList,errorTeacherIDList=self.otibe.submitInfo(filename)
                    print(repeatedTeacherIDList)
                    str1=''  #定义一个字符串，用来存储发生错误时的弹框内容
                    if len(repeatedTeacherIDList)!=0:  #有重复信息时
                        str1='工号为：'
                        for item in repeatedTeacherIDList:
                            str1+='{} '.format(item)
                        str1+='的教师信息已存在。'
                    if len(errorTeacherIDList)!=0:  #工号或时间输入不规范时
                        str1+='工号为：'
                        for item in errorTeacherIDList:
                            str1+='{} '.format(item)
                        str1+='的教师信息中，工号或时间输入不规范。'
                    if str1!='':
                        QMessageBox.information(self.ui, '', str1)
                    QMessageBox.information(self.ui,'操作成功','教师信息导入成功')
            else:
                QMessageBox.warning(self.ui,'出错了','上传的文件不能为空')
        except:
            QMessageBox.warning(self.ui,'操作有误','无法找到该文件')

    def cancel(self):
        self.ui.close()