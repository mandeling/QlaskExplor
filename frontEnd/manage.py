# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
import sys
from PyQt5.QtWidgets import QApplication
from windows.master import MainWindow

app = QApplication(sys.argv)
m = MainWindow()
m.show()
sys.exit(app.exec_())

