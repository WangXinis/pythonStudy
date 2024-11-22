import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# 定义主窗口的类
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个标签
        self.label = QLabel('Hello, World!', self)
        layout.addWidget(self.label)

        # 创建一个按钮
        btn = QPushButton('Click Me!', self)
        btn.clicked.connect(self.on_click)  # 连接按钮点击事件
        layout.addWidget(btn)

        self.setLayout(layout)  # 设置窗口布局
        self.setWindowTitle('PyQt5 Example')
        self.show()

    def on_click(self):
        self.label.setText('Button Clicked!')  # 改变标签的文本

# 运行应用程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())