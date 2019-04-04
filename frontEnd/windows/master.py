# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem, QAction
from widgets import FramelessWindow
from windows import HomePage, GetMachineCodeWindow, DialogCoverWindow, WebViewWindow


class MainWindow(FramelessWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        self.resize(1000, 620)
        self.setWindowIcon(QIcon("media/Qt.ico"))
        self.setWindowTitle("Qt功能试验工程")
        menu_1 = self.menuBar.setTopMenu("菜单1")
        action_1_1 = QAction("子菜单1", self)
        action_1_2 = QAction("子菜单2", self)
        menu_1.addAction(action_1_1)
        menu_1.addAction(action_1_2)
        menu_2 = self.menuBar.setTopMenu("菜单2")
        action_2_1 = QAction("子菜单1", self)
        menu_2.addAction(action_2_1)
        action_3_1 = QAction("子菜单1", self)
        action_3_2 = QAction("子菜单2", self)
        action_3_3 = QAction("子菜单3", self)
        action_3_4 = QAction("子菜单4", self)
        menu_3 = self.menuBar.setTopMenu("菜单3")
        menu_3.addActions([action_3_1, action_3_2, action_3_3, action_3_4])
        self.home = HomePage()  # 设置主页
        self.home.setListItem(QListWidgetItem("获取机器码"))  # 设置功能
        self.home.setListItem(QListWidgetItem("显示弹窗遮罩"))  # 设置功能
        self.home.setListItem(QListWidgetItem("功能导航按钮"))  # 设置功能
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
            elif item.text() == "功能导航按钮":
                try:
                    self.home.setView(WebViewWindow())
                except Exception as e:
                    print(e)

