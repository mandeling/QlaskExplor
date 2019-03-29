# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from PyQt5.QtWidgets import QWidget,QPushButton, QVBoxLayout,QDialog, QLabel
from PyQt5.QtCore import Qt


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
        button = QPushButton("弹窗遮罩")
        button.clicked.connect(self.show_dialog)
        layout.addWidget(button)
        self.setLayout(layout)


    def show_dialog(self):
        dialog = QDialog(self)
        dialog.resize(500,300)
        dialog.setWindowTitle("功能测试弹窗遮罩")
        dialog.setModal(True)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(QLabel('<font color="red">弹窗爽歪歪</font>'))
        dialog.setLayout(dialog_layout)
        mask = MaskWidget(self)
        mask.show()
        dialog.exec()
        mask.close()


