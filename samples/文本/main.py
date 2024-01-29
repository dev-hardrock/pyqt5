import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("Hello World")

    # 下面创建了一个Label,然后调用方法指定父类
    # label = QLabel("账号： ")
    # 设置父对象
    # label.setParent(w)

    # 下面创建了一个Label(纯文本)，在创建的时候指定了父对象
    label = QLabel("账号： ", w)

    # 显示Label的位置与大小： x, y, w, h
    label.setGeometry(20, 20, 30, 30)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
