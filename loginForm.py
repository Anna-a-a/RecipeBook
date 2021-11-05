import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from repository import *
from PyQt5 import uic
from mainForm import *
from addRecipeForm import *


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("loginForm.ui", self)
        self.initUI()

    def initUI(self):
        self.signInBtn.clicked.connect(self.signIn)
        self.repository = Repository()
        self.mainForm = MainWindow()

    def signIn(self):
        if self.repository.isUserExists(self.loginEdit.text(), self.passwordEdit.text()):
            QMessageBox.about(self, "Оповещение", "Удачно!")
            self.hide()
            self.mainForm.show()
        else:
            QMessageBox.about(self, "Оповещение", "Неудачно!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginForm = LoginForm()
    loginForm.show()
    sys.exit(app.exec())