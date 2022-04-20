import sys
from time import sleep
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MyWindow(QMainWindow):
    range_number = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("QThread学习")
        self.resize(800, 600)
        self.setup_ui()
        self.setup_thread()

    def setup_ui(self):
        self.mylistwidget = QListWidget(self)
        self.mylistwidget.resize(500, 500)
        self.mylistwidget.move(20, 20)

        self.additem_button = QPushButton(self)
        self.additem_button.resize(150, 30)
        self.additem_button.setText("填充QListWidget")
        self.additem_button.move(530, 20)

    def setup_thread(self):
        self.thread1 = QThread(self)  # 创建一个线程
        self.range_thread = WorkThread()  # 实例化线程类
        self.range_thread.moveToThread(self.thread1)  # 将类移动到线程中运行
        # 线程数据传回信号，用add_item函数处理
        self.range_thread.range_requested.connect(self.add_item)
        self.additem_button.clicked.connect(self.start_thread)
        self.range_number.connect(self.range_thread.range_proc)
        # self.additem_button.clicked.connect(self.range_thread.range_proc)  # 连接到线程类的函数

    def start_thread(self):
        self.thread1.start()
        range_number = 30
        self.range_number.emit(range_number)  # 发射信号让线程接收需要range多少

    def add_item(self, requested_number):  # 线程传回参数
        text = f"第{requested_number}项————Item"
        item = QListWidgetItem()
        item.setIcon(QPixmap())
        item.setText(text)
        self.mylistwidget.addItem(item)


class WorkThread(QObject):
    range_requested = Signal(int)  # 括号里是传出的参数的类型

    def __init__(self):
        super().__init__()

    def range_proc(self, number):  # number即为从主线程接收的参数
        print(number)
        for i in range(number):
            self.range_requested.emit(i)  # 发射信号
            sleep(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
