from PySide2.QtCore import QFile
from PySide2.QtWidgets import  QMessageBox
from controller.loginVerify import loginVerify
from utils.drawPie import drawPie
from PySide2.QtUiTools import QUiLoader

class loginWindow():
    def __init__(self,welcomeWindow):
        drawPie()
        qfile_stats = QFile('C:/Users/lenovo/Desktop/周报素材/新建文件夹/resources/ui/LoginWindow.ui')  # 打开ui文件
        self.welcomeWindow=welcomeWindow
        self.ui = QUiLoader().load(qfile_stats)  # 加载ui文件
        self.ui.Loginbutton.clicked.connect(self.loginTonext)

    def loginTonext(self):  # 登录界面点击登录按钮之后
        textname = self.ui.nameEdit.text()  # 所输入的用户名
        textpassword = self.ui.passwordEdit.text()  # 所输入的密码
        state=loginVerify(textname,textpassword)
        if state==0:
            self.welcomeWindow.show()
            self.ui.close()
        if state==1:
            QMessageBox.warning(self.ui, '出错了', '密码有误，请重新输入')
        if state==2:
            QMessageBox.warning(self.ui, '出错了', '账户不存在')
