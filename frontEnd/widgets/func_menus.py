# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


class FuncMenu(QWidget):
    def __init__(self):
        super(FuncMenu, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        style_sheet = """
        QPushButton {
            border:none;
            padding: 5px 15px;
            height: 25px;
            font-size:14px;
            font-weight: bold;
        }
        QPushButton:hover{
            background-color: rgb(200, 200, 200)
        }
        """
        # 支持qss设置背景
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout = QHBoxLayout(margin=0)
        self.setStyleSheet(style_sheet)
        self.setLayout(self.layout)

    def addMenu(self, menu):
        if not isinstance(menu, QPushButton):
            return
        self.layout.addWidget(menu)

    def addSpacer(self):
        self.layout.addSpacerItem(QSpacerItem(
            40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))


