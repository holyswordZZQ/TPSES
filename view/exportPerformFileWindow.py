from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidgetItem, QTableWidgetItem, QFileDialog
from PySide6.QtUiTools import QUiLoader
from controller.operateTeacherPerformController import operateTeacherPerformController
class exportPerformFileWindow:
    def __init__(self,performData):
        self.ui=QUiLoader().load('resources/ui/exportPerformFileWindow.ui')
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.performData=performData
        self.optc=operateTeacherPerformController()

        self.ui.openFileButton.clicked.connect(self.openFile)
        self.ui.exportPerformButton.clicked.connect(self.exportPerform)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def openFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)  # 设置文件过滤器，这里是任何文件，包括目录
        dialog.setViewMode(QFileDialog.Detail)  # 设置显示文件的模式，这里是详细模式
        dialog.setDefaultSuffix('.xlsx')
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.ui.fileNameEdit.setText(fileNames[0])

    def exportPerform(self):
        #try:
            fileName = self.ui.fileNameEdit.text()
            if fileName != '':
                self.optc.exportPerformToExcel(self.performData, fileName)
                QMessageBox.information(self.ui, '操作成功', '成功导出教师信息')
            else:
                QMessageBox.warning(self.ui, '操作失败', '文件名不能为空')
        #except:
            #QMessageBox.warning(self.ui, '操作有误', '文件名出现异常')

    def cancel(self):
        self.ui.close()