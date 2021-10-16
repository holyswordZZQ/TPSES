# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile, QSize
# from PySide6.QtGui import Qt, QPixmap, QPicture,QIcon
# import re
# from controller.operateTeacherInfo import getExistedTeacher
# from controller.operateTeacherInfo import operateTeacherInfo
#
# class deleteInfoWindow:
#     def __init__(self):
#         qfile_stats = QFile('resources/ui/deleteInfoWindow.ui')
#         self.oT=operateTeacherInfo()
#         self.ui = QUiLoader().load(qfile_stats)
#         self.ui.ensureButton.clicked.connect(self.delete)
#         self.ui.cancelButton.clicked.connect(self.cancel)
#
#     def delete(self):
#         textID = self.ui.idEdit.text()
#         print('text:' + textID)
#         m = re.match('\d\d\d\d\d\d\d\d', textID)  # 正则表达式判断输入的id是否规范
#         if m == None:
#             QMessageBox.warning(self.ui, '输入错误', '输入的id不符合要求')
#         else:
#             if not getExistedTeacher(textID + '.json'):
#                 QMessageBox.warning(self.ui, '出错了', 'id不存在，请先添加信息')
#             else:
#                 self.oT.deleteInfo(textID)
#                 QMessageBox.information(self.ui,'操作成功','删除成功')
#
#     def cancel(self):
#         self.ui.close()