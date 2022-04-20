import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
        self.set_list()

    def setup_ui(self):
        self.setWindowTitle("QListWidgetItem学习")
        self.resize(800, 600)

        self.listwidget = QListWidget(self)
        self.listwidget.resize(400, 500)
        self.listwidget.move(20, 20)
        self.listwidget.currentRowChanged.connect(self.change_select_item)

        self.label1 = QLabel(self)
        self.label1.resize(300, 30)
        self.label1.move(440, 20)

    def set_list(self):
        for i in range(10):
            item = QListWidgetItem()
            item.setIcon(QPixmap())
            item.setText(f"第{i}项Item，存储的data应为：{i}")
            item.setData(1, [f"第{i}项item的数据，由setData()创建，data()读取", f"检测list存储{i}"])
            self.listwidget.addItem(item)

    def change_select_item(self, current_index):
        item = self.listwidget.item(current_index)
        self.label1.setText(item.data(1)[1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
