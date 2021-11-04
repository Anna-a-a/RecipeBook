import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from data_base_functions import *
from PyQt5 import uic, QtWidgets


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface.ui", self)
        self.initUI()

    def initUI(self):
        self.signInBtn.clicked.connect(self.signIn)
        self.dataBase = DataBase()

    def signIn(self):
        if self.dataBase.isUserExists(self.loginEdit.text(), self.passwordEdit.text()):
            QMessageBox.about(self, "Оповещение", "Удачно!")
        else:
            QMessageBox.about(self, "Оповещение", "Неудачно!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())