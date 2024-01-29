import sys

from PyQt5.QtWidgets import QApplication, QWidget


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("Hello World")

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
