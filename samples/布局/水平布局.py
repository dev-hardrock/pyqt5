import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton


class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的__init__方法， 因为它里面有很多对UI控件的初始化操作
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 最外层的垂直布局，包含2部分：爱好和性别
        container = QVBoxLayout()

        # ----- 创建第一个组，添加多个组件 -----
        # hobby 主要是保证他们是一个组
        hobby_box = QGroupBox("爱好")

        # v_layout 保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()

        btn1 = QRadioButton("抽烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("烫头")

        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)

        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # ----- 创建第二个组，添加多个组件 -----
        # 性别组
        gender_box = QGroupBox("性别")

        # 性别容器
        h_layout = QVBoxLayout()

        # 性别选项
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")

        # 添加到h_layout中
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)

        # 把h_layout添加到gender_box中
        gender_box.setLayout(h_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        # 设置窗口显示的内容是最外层的容器
        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
