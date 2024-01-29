import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("Hello World")

    # 下面创建了一个Label(纯文本)，在创建的时候指定了父对象
    label = QLabel("账号： ", w)

    # 显示Label的位置与大小： x, y, w, h
    label.setGeometry(20, 20, 30, 30)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(55, 20, 200, 20)

    # 在窗口里面添加控件
    btn = QPushButton("注册", w)
    btn.setGeometry(50, 80, 70, 30)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
