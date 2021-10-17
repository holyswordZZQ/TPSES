from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize
from PySide6.QtGui import Qt, QPixmap, QPicture,QIcon
from controller.operateTeacherInfoController import operateTeacherInfo
from view.showPerforWindow import showPerforWindow
from view.addInfoWindow import addInfoWindow
from view.modifyDetailWindow import modifyDetailWindow
from view.importFileWindow import importFileWindow
from view.exportTeacherInfoWindow import exportTeacherInfoWindow




class teacherInfoWindow:  # 二级功能界面设计

    def __init__(self):
        #创建controller对象,获取数据
        self.ot=operateTeacherInfo()
        self.data = self.ot.getTeacherInfo()
        print(self.data)
        #ui设置
        self.ui = QUiLoader().load('resources/ui/jiemian2.ui')
        self.image=QPixmap()
        self.image.load('resources/images/teacherInfoWindow.png')
        self.ui.imageLabel.setPixmap(self.image)
        self.flag=1             #flag控制排序
        self.button1=QIcon('resources/images/三角1.svg')
        self.button2=QIcon('resources/images/三角2.svg')
        self.ui.sortButton.setIcon(self.button1)
        self.ui.sortButton.clicked.connect(self.showSortedInfo)
        self.ui.comboBox_xueyuan.currentIndexChanged.connect(self.refreshTableByConditions)
        self.ui.comboBox_zhicheng.currentIndexChanged.connect(self.refreshTableByConditions)
        self.ui.search_button.clicked.connect(self.refreshTableByConditions)
        self.ui.search_text.returnPressed.connect(self.refreshTableByConditions)   # 设置回车连接
        self.ui.add_account_button.clicked.connect(self.goToAdd)
        self.ui.deleteButton.clicked.connect(self.goToDelete)
        self.ui.modify_account_button.clicked.connect(self.goToDetailmodify)
        self.ui.refreshButton.clicked.connect(self.refresh)
        self.ui.searchButton.clicked.connect(self.gotoPerform)
        self.ui.excelImportButton.clicked.connect(self.excelImport)
        self.ui.exportButton.clicked.connect(self.excelExport)


        self.show_all_information()

        self.addInfoWindow=addInfoWindow()
        self.showperforwindow=None
        self.modifyDetailWindow=None
        self.importfilewindow=None
        self.exportteacherinfowindow=None

    # 将列表中所有教师的简略基本信息显示在表格中
    def show_all_information(self):
        self.ui.table.setRowCount(0)
        for i in range(len(self.data)):
            if self.data[i][6]=='1':
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

                time = QTableWidgetItem(self.data[i][5])
                time.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
                time.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
                self.ui.table.setItem(rowcount, 4, time)

    #按时间排序的响应函数
    def showSortedInfo(self):
        if self.flag==1:
            self.ui.sortButton.setIcon(self.button2)
            self.data=self.ot.sortByTime(self.data,bool(self.flag))
        else:
            self.ui.sortButton.setIcon(self.button1)
            self.data = self.ot.sortByTime(self.data, bool(self.flag))
        self.flag=1-self.flag
        self.show_all_information()

    #搜索框模糊搜索结果更新
    def refreshTableByConditions(self):
        keyText=self.ui.search_text.text()
        college=self.ui.comboBox_xueyuan.currentText()
        title=self.ui.comboBox_zhicheng.currentText()
        self.data=self.ot.getTeacherInfoByConditions(keyText,college,title)
        self.show_all_information()


    def getSelectedRanges(self):
        listItem=self.ui.table.selectedItems()
        selectedItem=[]
        for item in listItem:
            selectedItem.append(item.text())
        return selectedItem

    def gotoPerform(self):
        list = self.getSelectedRanges()
        self.showperforwindow = showPerforWindow(list)
        self.showperforwindow.ui.show()


    def goToAdd(self):  #添加信息界面
        self.addInfoWindow.ui.show()

    def goToDetailmodify(self):  #修改信息页面
        selectedItems=self.getSelectedRanges()
        if len(selectedItems)==1:
            print(selectedItems)
            self.modifyDetailWindow=modifyDetailWindow(selectedItems[0],self.data)
            self.modifyDetailWindow.ui.show()
        else:
            QMessageBox.warning(self.ui,'Wrong!','hahaha')

    def goToDelete(self):
        list=self.getSelectedRanges()
        if list!=None or list!=[]:
            self.ot.deleteInfo(list)
            QMessageBox.information(self.ui,'操作成功','删除成功')

    def refresh(self):  #刷新信息
        self.data=self.ot.getTeacherInfo()
        self.show_all_information()
        self.ui.search_text.setText('')
        self.ui.comboBox_xueyuan.setCurrentText('全部')
        self.ui.comboBox_zhicheng.setCurrentText('全部')

    def excelImport(self):

        self.importfilewindow=importFileWindow()
        self.importfilewindow.ui.show()

    def excelExport(self):
        self.exportteacherinfowindow=exportTeacherInfoWindow(self.data)
        self.exportteacherinfowindow.ui.show()


