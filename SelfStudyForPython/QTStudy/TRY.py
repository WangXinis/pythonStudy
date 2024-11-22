import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
 
# 创建应用程序对象
app = QApplication(sys.argv)
 
# 创建一个窗口对象
window = QWidget()
 
# 创建一个按钮对象并将其添加到窗口中
button = QPushButton('点击我')
button.move(100, 50)  # 设置按钮的位置
button.clicked.connect(lambda: print('按钮被点击了'))  # 当按钮被点击时，打印信息
 
# 设置窗口的大小
window.resize(400, 200)
 
# 显示窗口
window.show()
 
# 进入应用程序的主循环，等待事件处理
sys.exit(app.exec_())