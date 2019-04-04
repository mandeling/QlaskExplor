# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QMenuBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from widgets import ToolWidget, FuncMenu


class WebViewWindow(QWidget):
    def __init__(self):
        super(WebViewWindow, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        ver_layout = QVBoxLayout(margin=0, spacing=0)  # 竖直布局,控件间距为0, 上下间距为0
        func_menu = FuncMenu()  # 功能按钮
        func_menu.setMaximumHeight(30)  # 固定高度
        button_1 = QPushButton("功能1")
        button_2 = QPushButton("功能2")
        button_3 = QPushButton("功能3")
        func_menu.addMenu(button_1)
        func_menu.addMenu(button_2)
        func_menu.addMenu(button_3)
        # 按钮点击关联槽函数
        button_1.clicked.connect(self.button_1_func)
        button_2.clicked.connect(self.button_2_func)
        button_3.clicked.connect(self.button_3_func)
        # 右边伸缩条
        func_menu.addSpacer()
        self.web_view = QWebEngineView()  # 可视网页控件
        self.web_view.setContentsMargins(0, 0, 0, 0)
        self.web_view.load(QUrl("file:///html/index.html"))
        ver_layout.addWidget(func_menu)  # 上边功能按钮

        wt_layout = QHBoxLayout()  # wt: web and tools
        tools = ToolWidget()
        tools.setMaximumWidth(50)
        tool_button_1 = QPushButton("工具1")
        tool_button_2 = QPushButton("工具2")
        tool_button_3 = QPushButton("工具3")
        tools.layout.addStretch(2)
        tools.addTool(tool_button_1)
        tools.addTool(tool_button_2)
        tools.addTool(tool_button_3)
        tools.layout.addStretch(6)
        wt_layout.addWidget(self.web_view)
        wt_layout.addWidget(tools)
        ver_layout.addLayout(wt_layout)
        # ver_layout.addWidget(self.web_view)
        self.setLayout(ver_layout)

    def button_1_func(self):
        self.web_view.load(QUrl("file:///html/func1.html"))

    def button_2_func(self):
        self.web_view.load(QUrl("file:///html/func2.html"))

    def button_3_func(self):
        self.web_view.load(QUrl("file:///html/func3.html"))

