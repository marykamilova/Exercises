# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random
from datetime import datetime


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def button_clicked(self):
        with open('aff.txt', 'r') as f:
            affs = f.readlines()
        aff = affs[datetime.now().weekday()]
        self.label.setText(aff)
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 150)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Daily affirmation!")
        self.b1.setGeometry(170, 50, 160, 50)
        self.b1.clicked.connect(self.button_clicked)

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()