from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem, \
    QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize
from PySide6.QtGui import Qt, QPixmap, QPicture,QIcon
from controller.operateTeacherInfoByExcelController import operateTeacherInfoByExcelController

class exportTeacherInfoWindow:
    def __init__(self,data):
        self.ui = QUiLoader().load('resources/ui/exportTeacherInfoDialog.ui')
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.data=data

        self.otibe = operateTeacherInfoByExcelController()

        self.ui.openFileButton.clicked.connect(self.openFile)
        self.ui.exportInfoButton.clicked.connect(self.exportTeacherInfo)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def openFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)  # 设置文件过滤器，这里是任何文件，包括目录
        dialog.setViewMode(QFileDialog.Detail)  # 设置显示文件的模式，这里是详细模式
        dialog.setDefaultSuffix('.xlsx')
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.ui.fileNameEdit.setText(fileNames[0])

    def exportTeacherInfo(self):
        try:
            fileName=self.ui.fileNameEdit.text()
            if fileName!='':
                self.otibe.exportToExcel(self.data,fileName)
                QMessageBox.information(self.ui,'操作成功','成功导出教师信息')
            else:
                QMessageBox.warning(self.ui,'操作失败','文件名不能为空')
        except:
            QMessageBox.warning(self.ui,'操作有误','文件名出现异常')

    def cancel(self):
        self.ui.close()