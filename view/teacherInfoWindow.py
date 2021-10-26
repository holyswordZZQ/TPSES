from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize
from PySide6.QtGui import Qt, QPixmap, QPicture,QIcon
from controller.operateTeacherInfoController import operateTeacherInfoController
from view.showPerforWindow import showPerforWindow
from view.addInfoWindow import addInfoWindow
from view.modifyDetailWindow import modifyDetailWindow
from view.importFileWindow import importFileWindow
from view.exportTeacherInfoWindow import exportTeacherInfoWindow




class teacherInfoWindow:  # 二级功能界面设计

    def __init__(self):
        #创建controller对象,获取数据
        self.otic=operateTeacherInfoController()
        self.data = self.otic.getTeacherInfo()
        print(self.data)
        #ui设置
        self.ui = QUiLoader().load('resources/ui/showTeacherInfoWindow.ui')
        self.image=QPixmap()
        self.image.load('resources/images/teacherInfoWindow.png')
        self.ui.imageLabel.setPixmap(self.image)
        self.flag=1             #flag控制排序
        self.button1=QIcon('resources/images/三角1.svg')
        self.button2=QIcon('resources/images/三角2.svg')

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
        self.ui.table.setSortingEnabled(False)
        count=self.ui.table.rowCount()
        for i in range(count):
            self.ui.table.removeRow(count-i-1)

        for i in range(len(self.data)):
                rowcount = self.ui.table.rowCount()  # 获取当前的行数
                self.ui.table.insertRow(rowcount)  # 在末尾插入新的一行
                # 加入信息
                id = QTableWidgetItem(self.data[i].id)
                # id.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
                id.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
                self.ui.table.setItem(rowcount, 0, id)  # 将信息插入表格

                name = QTableWidgetItem(self.data[i].name)
                name.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
                name.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
                self.ui.table.setItem(rowcount, 1, name)

                # 显示学院信息
                college = QTableWidgetItem(self.data[i].college)
                college.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
                college.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
                self.ui.table.setItem(rowcount, 2, college)

                # 显示职称信息
                title = QTableWidgetItem(self.data[i].title)
                title.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
                title.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
                self.ui.table.setItem(rowcount, 3, title)

                time = QTableWidgetItem(self.data[i].time)
                time.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
                time.setTextAlignment(Qt.AlignHCenter)  # 设置文本居中
                self.ui.table.setItem(rowcount, 4, time)

                available=QTableWidgetItem("否" if self.data[i].available=='0' else "是")
                available.setFlags(Qt.ItemIsEnabled)
                available.setTextAlignment(Qt.AlignHCenter)
                self.ui.table.setItem(rowcount,5,available)
        self.ui.table.setSortingEnabled(True)

    #搜索框模糊搜索结果更新
    def refreshTableByConditions(self):
        keyText=self.ui.search_text.text()
        college=self.ui.comboBox_xueyuan.currentText()
        title=self.ui.comboBox_zhicheng.currentText()
        self.data=self.otic.getTeacherInfoByConditions(keyText,college,title)
        self.ui.table.setSortingEnabled(False)
        self.show_all_information()
        self.ui.table.setSortingEnabled(True)

    def getSelectedRanges(self):
        listItem=self.ui.table.selectedItems()
        selectedItem=[]
        for item in listItem:
            selectedItem.append(item.text())
        print(selectedItem)
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
            self.modifyDetailWindow=modifyDetailWindow(selectedItems[0],self.data)
            self.modifyDetailWindow.ui.show()
        else:
            QMessageBox.warning(self.ui,'出错啦！','你不能一次修改多个老师的信息噢')

    def goToDelete(self):
        list=self.getSelectedRanges()
        print(list)
        if list!=None and list!=[]:
            self.otic.deleteInfo(list)
            QMessageBox.information(self.ui,'操作成功','删除成功')

    def refresh(self):  #刷新信息
        self.data=self.otic.getTeacherInfo()
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


