from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import Qt
from controller.operateTeacherInfo import operateTeacherInfo

class teacherInfoWindow:  # 二级功能界面设计
    def __init__(self,addInfoWindow,modifyInfoWindow):
        self.ot=operateTeacherInfo()
        self.ui = QUiLoader().load('resources/ui/jiemian_2.ui')
        self.addInfoWindow=addInfoWindow
        self.modifyInfoWindow=modifyInfoWindow

        self.data=self.ot.getTeacherInfo()
        self.show_all_information()
        # 当前下拉框发生改变后进行更新表单
        self.ui.comboBox_xueyuan.currentIndexChanged.connect(self.update_table)
        self.ui.comboBox_zhicheng.currentIndexChanged.connect(self.update_table)
        # 二级到三级的跳转
        #self.ui.table.clicked.connect(self.tiaozhuan)

        # 精确查询
        self.ui.search_button.clicked.connect(self.search_person)
        self.ui.search_text.returnPressed.connect(self.search_person)  # 设置回车连接

        # 设置重置按钮
        self.ui.shuaxin_button.clicked.connect(lambda: self.show_all_information(self.dict_list))

        # 设置新增按钮
        self.ui.add_account_button.clicked.connect(self.goToAdd)

        # 设置修改按钮
        self.ui.modify_account_button.clicked.connect(self.goTomodify)
        self.ui.refreshButton.clicked.connect(self.refresh)
        #self.ui.addperformanceButton.clicked.connect(self.addPerformance)

    def show_all_information(self):
        # 将列表中所有教师的简略基本信息显示在表格中
        self.ui.table.setRowCount(0)
        for i in range(len(self.data)):
            rowcount = self.ui.table.rowCount()  # 获取当前的行数
            self.ui.table.insertRow(rowcount)  # 在末尾插入新的一行
            # 加入信息
            id = QTableWidgetItem(self.data[i][0])
            # id.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            id.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 0, id)  # 将信息插入表格

            name = QTableWidgetItem(self.data[i][1])
            name.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            name.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 1, name)

            # 显示学院信息
            college = QTableWidgetItem(self.data[i][2])
            college.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            college.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 2, college)

            # 显示职称信息
            title = QTableWidgetItem(self.data[i][3])
            title.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            title.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 3, title)

    def search_person(self):  # 根据教师信息来精确查询

        text = self.ui.search_text.text()  # 获取单元格内容
        # flag = False  # 设置是否已经查到的标志
        self.ui.table.setRowCount(0)  # 格式化表单
        self.data=self.ot.searchTeaherInfo(text)
        self.show_all_information()
        # print(flag)

    def update_table(self):
        self.ui.table.setRowCount(0)  # 每次刷新表单时重置表格
        college = self.ui.comboBox_xueyuan.currentText()  # 获取学院下拉框的内容
        title = self.ui.comboBox_zhicheng.currentText()  # 获取职称下拉框的内容
        length = len(self.dict_list)  # 获取总人数，也就是总文件数

        selectFilter={
            'college':college,
            'title':title
        }
        self.data=self.ot.getTeacherByAttribute(selectFilter)
        self.show_all_information()

    # def addPerformance(self):   #添加履历信息界面
    #     addperformancewindow.ui.show()
    # def tiaozhuan(self):
    #     for i in self.ui.table.selectedItems():
    #         global m
    #         m=i.text()
    #         global allinformation
    #         allinformation=allInformation()
    #         allinformation.ui.show()


    def goToAdd(self):  #添加信息界面
        self.addInfoWindow.ui.show()

    def goTomodify(self):  #修改信息页面
        self.modifyInfoWindow.ui.show()

    def refresh(self):  #刷新信息
        self.data=self.ot.getTeacherInfo()
        self.ui.table.setRowCount(0)  #格式化表格
        for i in range(len(self.data)):
            rowcount = self.ui.table.rowCount()  # 获取当前的行数
            self.ui.table.insertRow(rowcount)  # 在末尾插入新的一行
            # 加入信息
            id = QTableWidgetItem(self.data[i][0])
            # id.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            id.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 0, id)  # 将信息插入表格

            name = QTableWidgetItem(self.data[i][1])
            name.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            name.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 1, name)

            # 显示学院信息
            college = QTableWidgetItem(self.data[i][2])
            college.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            college.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 2, college)

            # 显示职称信息
            title = QTableWidgetItem(self.data[i][3])
            title.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
            title.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
            self.ui.table.setItem(rowcount, 3, title)
