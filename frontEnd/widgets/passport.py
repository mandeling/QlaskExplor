# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from PyQt5.QtWidgets import QDialog, QWidget, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox,QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QColor, QFont, QIcon

StyleSheet = """
/*标题栏*/
TitleBar {
    background-color: rgb(54, 157, 180);
}

/*最小化最大化关闭按钮通用默认背景*/
#buttonMinimum,#buttonMaximum,#buttonClose {
    border: none;
    background-color: rgb(54, 157, 180);
}

/*悬停*/
#buttonMinimum:hover,#buttonMaximum:hover {
    background-color: rgb(48, 141, 162);
}
#buttonClose:hover {
    color: rgb(150, 180, 150);
    /*background-color: rgb(150, 150, 130);*/
}

/*鼠标按下不放*/
#buttonMinimum:pressed,#buttonMaximum:pressed {
    background-color: rgb(44, 125, 144);
}
#buttonClose:pressed {
    color: white;
    background-color: rgb(161, 73, 92);
}
"""


class TitleBar(QWidget):
    # 窗口最小化信号
    # windowMinimumed = pyqtSignal()
    # 窗口最大化信号
    # windowMaximumed = pyqtSignal()
    # 窗口还原信号
    # windowNormaled = pyqtSignal()
    # 窗口关闭信号
    windowClosed = pyqtSignal()
    # 窗口移动
    windowMoved = pyqtSignal(QPoint)  # 删掉即报错，不发出信号即可

    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)
        self.setStyleSheet(StyleSheet)
        # 支持qss设置背景
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.mPos = None
        self.iconSize = 20  # 图标的默认大小
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self.setPalette(palette)
        # 布局
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        # 窗口图标
        self.iconLabel = QLabel(self)
#         self.iconLabel.setScaledContents(True)
        layout.addWidget(self.iconLabel)
        # 窗口标题
        self.titleLabel = QLabel(self)
        self.titleLabel.setMargin(2)
        layout.addWidget(self.titleLabel)
        # 中间伸缩条
        layout.addSpacerItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        # 利用Webdings字体来显示图标
        font = self.font() or QFont()
        font.setFamily('Webdings')
        # 关闭按钮
        self.buttonClose = QPushButton(
            'r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
        layout.addWidget(self.buttonClose)
        # 初始高度
        self.setHeight()

    def setHeight(self, height=42):
        """设置标题栏高度"""
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        self.buttonClose.setMinimumSize(height, height)
        self.buttonClose.setMaximumSize(height, height)

    def setTitle(self, title):
        """设置标题"""
        self.titleLabel.setText(title)

    def setIcon(self, icon):
        """设置图标"""
        self.iconLabel.setPixmap(icon.pixmap(self.iconSize, self.iconSize))

    def setIconSize(self, size):
        """设置图标大小"""
        self.iconSize = size

    def enterEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super(TitleBar, self).enterEvent(event)

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()


class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        self.style_sheet = """
            LoginDialog {
                border:1px solid rgb(54, 157, 180)
                }
            
            QLineEdit {
                /*background:transparent;*/
                border-width:0;
                border-style:outset;
                border-top:1px solid rgb(54, 157, 150);
                border-bottom:1px solid rgb(54, 157, 150)
            }
            /*
            QLabel {
                border-top:1px solid rgb(54, 157, 150);
                border-bottom:1px solid rgb(54, 157, 150)
            }
            */
        """
        self.resize(500, 400)
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # layout = QVBoxLayout(self)
        # layout.setContentsMargins(0, 0, 0, 0)
        # 添加个head
        title_bar = TitleBar(self)
        title_bar.setGeometry(0, 0, 500, 42)
        title_bar.windowClosed.connect(self.close)
        title_bar.windowMoved.connect(self.move)
        label_1 = QLabel(self)
        label_1.setStyleSheet("image:url(media/user_icon.jpg)")
        label_1.setGeometry(100, 100, 36, 35)
        label_2 = QLabel(self)
        label_2.setStyleSheet("image:url(media/mima_icon.jpg)")
        label_2.setGeometry(100, 150, 36, 35)
        edit_1 = QLineEdit(self)
        edit_1.setGeometry(136, 100, 200, 35)
        edit_2 = QLineEdit(self)
        edit_2.setEchoMode(QLineEdit.Password)
        edit_2.setGeometry(136, 150, 200, 35)
        button_1 = QPushButton("登录", self)
        button_1.setGeometry(100, 250, 100, 25)
        button_1.clicked.connect(self.login)
        button_2 = QPushButton("取消", self)
        button_2.setGeometry(250, 250, 100, 25)
        button_2.clicked.connect(self.cancel)
        self.windowTitleChanged.connect(title_bar.setTitle)
        self.windowIconChanged.connect(title_bar.setIcon)

        self.setWindowIcon(QIcon("media/Qt.ico"))
        self.setStyleSheet(self.style_sheet)

    def login(self):
        QMessageBox.information(self, "成功", "登录成功")

    def cancel(self):
        self.close()


class RegisterDialog(QDialog):
    def __init__(self):
        super(RegisterDialog, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        style_sheet = """
            RegisterDialog {
                border:1px solid rgb(54, 157, 180);
            }
        """
        self.resize(500, 400)
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 添加个head
        title_bar = TitleBar(self)
        title_bar.setGeometry(0, 0, 500, 42)
        title_bar.windowClosed.connect(self.close)
        title_bar.windowMoved.connect(self.move)
        self.windowTitleChanged.connect(title_bar.setTitle)
        self.windowIconChanged.connect(title_bar.setIcon)
        self.setWindowIcon(QIcon("media/Qt.ico"))
        self.setStyleSheet(style_sheet)






