import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QApplication

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 使用grid布局显示界面
        grid = QGridLayout()
        self.setLayout(grid)
        # 定义按钮显示内容
        names = ['', '', '', 'cls',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            # 设置button的点击事件处理方法(signal/slot)
            button.clicked.connect(self.on_button_clicked)
            grid.addWidget(button, *position)

        # 设置显示结果的输入框
        self.resultLineEdit = QLineEdit()
        self.resultLineEdit.setReadOnly(True)
        grid.addWidget(self.resultLineEdit, 0, 0, 1, 3)

        self.move(300, 150)
        self.setWindowTitle('计算机')
        self.show()

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()
        if text == '':
            return
        elif text in "0123456789+-*/.":
            self.resultLineEdit.insert(text)
        elif text in "=":
            try:
                self.resultLineEdit.insert('={result}'.format(
                    result=eval(self.resultLineEdit.text())))
            except:
                self.resultLineEdit.setText("some error occurs, press cls!")
        elif text in "cls":
            self.resultLineEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
