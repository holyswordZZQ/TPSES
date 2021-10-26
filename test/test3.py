import sys
from PySide6.QtCore import Signal, QObject, QCoreApplication


class StandardItem(QObject):
    # 定义信号，信号有两个参数，两个参数的类型分别为str,str，信号名称为dataChanged
    data_changed = Signal(str, str, name="dataChanged")

    # 更新信息，发送信号
    def update(self):
        self.dataChanged.emit("old status", "new status")

    # 定义槽函数
def onDataChanged(haha=None,xixi=None):
    print('1')
    print(haha)
    print(xixi)


if __name__ == "__main__":
    app=QCoreApplication([])
    item=StandardItem()
    item.data_changed.connect(onDataChanged)
    item.update()
    sys.exit(app.exec())