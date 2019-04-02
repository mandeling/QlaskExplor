# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from PyQt5.QtWidgets import QWidget,QPushButton, QVBoxLayout,QDialog, QLabel
from PyQt5.QtCore import Qt
from widgets import LoginDialog, RegisterDialog


class MaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet('background:rgba(0,0,0,102);')
        self.setAttribute(Qt.WA_DeleteOnClose)

    def show(self):
        """重写show，设置遮罩大小与parent一致
        """
        if self.parent() is None:
            return
        parent_rect = self.parent().geometry()
        self.setGeometry(0, 0, parent_rect.width(), parent_rect.height())
        super().show()


class DialogCoverWindow(QWidget):

    def __init__(self):
        super(DialogCoverWindow, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        layout = QVBoxLayout()
        button_1 = QPushButton("登录")
        button_2 = QPushButton("注册")
        button_1.clicked.connect(self.login_dialog)
        button_2.clicked.connect(self.register_dialog)
        layout.addWidget(button_1)
        layout.addWidget(button_2)
        self.setLayout(layout)

    def register_dialog(self):
        dialog = RegisterDialog()
        dialog.setWindowTitle("注册")
        dialog.setModal(True)
        mask = MaskWidget(self)
        mask.show()
        dialog.exec()
        mask.close()

    def login_dialog(self):
        dialog = LoginDialog()
        dialog.setWindowTitle("登录")
        dialog.setModal(True)
        mask = MaskWidget(self)
        mask.show()
        dialog.exec()
        mask.close()


