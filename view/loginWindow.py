
from PySide6.QtGui import QPalette, QBrush, QPixmap
from PySide6.QtWidgets import QMessageBox, QMainWindow
from controller.loginVerify import loginVerify
#from utils.drawPie import drawPie
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet, QtStyleTools

class loginWindow:
    def __init__(self,mainWindow):
        #drawPie()  # 打开ui文件

        self.ui = QUiLoader().load('resources/ui/LoginWindow.ui')  # 加载ui文件
        # apply_stylesheet(self.ui, 'light_blue.xml', invert_secondary=True,extra=extra)
        # stylesheet = self.ui.styleSheet()
        # with open('resources/loginWindow.css') as file:
        #     self.ui.setStyleSheet(stylesheet+file.read())
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.Loginbutton.clicked.connect(self.loginTonext)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("resources/images/loginWindow.jpg")))
        self.ui.setPalette(palette)
        self.mainWindow = mainWindow

    def loginTonext(self):  # 登录界面点击登录按钮之后
        textname = self.ui.nameEdit.text()  # 所输入的用户名
        textpassword = self.ui.passwordEdit.text()  # 所输入的密码
        state=loginVerify(textname,textpassword)
        if state==0:
            self.mainWindow.show()
            self.ui.close()
        if state==1:
            QMessageBox.warning(self.ui, '出错了', '密码有误，请重新输入')
        if state==2:
            QMessageBox.warning(self.ui, '出错了', '账户不存在')
