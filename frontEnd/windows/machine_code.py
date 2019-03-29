# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
import hashlib
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout
from windows.utils import machine


class GetMachineCodeWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(GetMachineCodeWindow, self).__init__(*args, **kwargs)
        self.__init_ui()

    def __init_ui(self):
        self.is_added = False
        self.machine_code = QTextEdit()
        get_code_btn = QPushButton("获取机器码")
        get_code_btn.clicked.connect(self.get_machine_code)
        ver_layout = QVBoxLayout()
        ver_layout.addWidget(get_code_btn)
        ver_layout.addWidget(self.machine_code)
        self.setLayout(ver_layout)

    def get_machine_code(self):
        md = hashlib.md5()
        main_board = machine.main_board()
        disk = machine.disk()
        md.update(main_board.encode("utf-8"))
        md.update(disk.encode("utf-8"))
        self.machine_code.setText(md.hexdigest())


