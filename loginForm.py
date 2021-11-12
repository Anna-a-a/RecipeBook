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
        self.signUpBtn.clicked.connect(self.signUp)
        self.mainForm = MainWindow()
        repository = Repository()
        self.mainForm.repository = repository
        self.repository = repository

    #logging in and checking for user availability
    def signIn(self):
        if self.repository.isUserExists(self.loginEdit.text(), self.passwordEdit.text()):
            userId = self.repository.getUserIdByLogin(self.loginEdit.text())
            self.mainForm.initPage(self.loginEdit.text(), userId)
            self.hide()
            self.mainForm.show()
        else:
            QMessageBox.about(self, "Оповещение", "Неверно введен логин или пароль")

    #registration and verification of account availability in the system
    def signUp(self):
        if not self.repository.isUserExists(self.loginEdit.text(), self.passwordEdit.text()):
                countOfUsers = self.repository.getUsersMaxId()[0] + 1
                self.repository.addUser(countOfUsers, self.loginEdit.text(), self.passwordEdit.text())
                QMessageBox.about(self, "Оповещение", "Регистрация успешна, войдите в свой аккаунт")

        else:
            QMessageBox.about(self, "Оповещение", "Вы зарегестрированы")
        self.loginEdit.clear()
        self.passwordEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginForm = LoginForm()
    loginForm.show()
    sys.exit(app.exec())