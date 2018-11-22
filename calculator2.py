#coding: utf-8

from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QApplication, QMainWindow, QActionGroup, QAction
import sys
import os
import qdarkstyle
import qdarkgraystyle
# import PyQt5_stylesheets
app = None

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('calculator.ui', self)

        actionGroupDefaultStyle = QActionGroup(self)
        actionGroupDefaultStyle.addAction(self.actionFusion)
        actionGroupDefaultStyle.addAction(self.actionWindows)
        actionGroupDefaultStyle.addAction(self.actionWindowsVista)
        actionGroupDefaultStyle.setExclusive(True)

        actionGroupStyle = QActionGroup(self)
        actionGroupStyle.addAction(self.actionQdarkstyle)
        actionGroupStyle.addAction(self.actionQdarkgraystyle)
        actionGroupStyle.addAction(self.actionMyStyle)
        actionGroupStyle.addAction(self.actionResetStyle)
        actionGroupStyle.setExclusive(True)

        self.show()

    @pyqtSlot()
    def on_action_triggered(self):
        action = self.sender()
        text = action.text()
        if text == "Exit":
            app.quit()
        elif text == "Fusion":
            app.setStyle('Fusion')
        elif text == "Windows":
            app.setStyle('Windows')
        elif text == "WindowsVista":
            app.setStyle('WindowsVista')
        elif text == "Qdarkstyle":
            # https://github.com/ColinDuquesnoy/QDarkStyleSheet
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        elif text == "Qdarkgraystyle":
            # https://github.com/mstuttgart/qdarkgraystyle
            self.setStyleSheet(qdarkgraystyle.load_stylesheet())
        elif text == "MyStyle":
            self.setStyleSheet(open('style/material/material-blue.qss').read())
        elif text == "ResetStyle":
            self.setStyleSheet("")

    @pyqtSlot()
    def on_button_clicked(self):
        button = self.sender()
        text = button.text()
        if text == '':
            return
        elif text in "0123456789+-*/.":
            self.lineEditResult.insert(text)
        elif text in "=":
            try:
                self.lineEditResult.insert('={result}'.format(
                    result=eval(self.lineEditResult.text())))
            except:
                self.lineEditResult.setText("some error occurs, press cls!")
        elif text in "cls":
            self.lineEditResult.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
