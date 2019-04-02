# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem, QMenuBar
from widgets import FramelessWindow
from windows import HomePage, GetMachineCodeWindow, DialogCoverWindow


class MainWindow(FramelessWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        self.resize(1000, 620)
        self.setWindowIcon(QIcon("media/Qt.ico"))
        self.setWindowTitle("Qt功能试验工程")
        self.home = HomePage()  # 设置主页
        self.home.setListItem(QListWidgetItem("获取机器码"))  # 设置功能
        self.home.setListItem(QListWidgetItem("显示弹窗遮罩"))  # 设置功能
        self.home.function_list.clicked.connect(self.choose_function)
        self.setWidget(self.home)  # 显示窗口内容

    def choose_function(self):
        """功能选择"""
        item = self.home.function_list.currentItem()
        if item:
            if item.text() == "获取机器码":
                self.home.setView(GetMachineCodeWindow())
            elif item.text() == "显示弹窗遮罩":
                self.home.setView(DialogCoverWindow())


