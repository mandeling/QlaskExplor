# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle

from PyQt5.QtWidgets import QWidget,QHBoxLayout,QListWidgetItem, QListWidget, QVBoxLayout


class HomePage(QWidget):
    def __init__(self):
        super(HomePage, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        self.hor_layout = QHBoxLayout()
        self.view_layout = QVBoxLayout()
        self.hor_layout.setContentsMargins(0, 0, 0, 0)
        self.function_list = QListWidget()
        self.function_list.setStyleSheet("QListWidget{border:none;}")
        self.function_list.setMaximumWidth(200)
        self.hor_layout.addWidget(self.function_list)
        self.hor_layout.addLayout(self.view_layout)
        self.setLayout(self.hor_layout)

    def setListItem(self, func):
        if not isinstance(func, QListWidgetItem):
            raise ValueError("the object must be instance of `QListWidgetItem`")
        self.function_list.addItem(func)

    def setView(self, window):
        if not isinstance(window, QWidget):
            raise ValueError("the object must be instance of `QWidget`")
        self.view_layout.addWidget(window)


