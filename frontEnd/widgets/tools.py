# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


class ToolWidget(QWidget):
    def __init__(self):
        super(ToolWidget, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        style_sheet = """
            ToolWidget {
                background-color: rgb(252, 252, 252);
            }
            QPushButton{
                background-color: #FFFFFF;
                margin: 5px 0;
                padding: 5px 0;
            }
        """
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置了才能使用qss设置布局背景色
        self.layout = QVBoxLayout(spacing=0, margin=0)
        self.setLayout(self.layout)
        self.setStyleSheet(style_sheet)

    def addTool(self, tool):
        if not isinstance(tool, QPushButton):
            return
        self.layout.addWidget(tool, alignment=Qt.AlignTop)




