import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("Hello World")

    # 设置图标
    w.setWindowIcon(QIcon('test.png'))

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
