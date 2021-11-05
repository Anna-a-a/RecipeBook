import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QComboBox
from PyQt5 import QtGui
from loginForm import *
from addRecipeForm import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addRecipeForm = AddRecipeForm()
        self.setGeometry(500, 300, 800, 500)
        self.setWindowTitle('Recipe Book')

        self.mainLabel = QLabel(self)
        self.mainLabel.resize(300, 50)
        self.mainLabel.move(250, 0)
        self.mainLabel.setText("Your Recipe book")
        self.mainLabel.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))

        self.cmb = QComboBox(self)
        self.cmb.resize(110, 28)
        self.cmb.move(10, 51)


        self.addRecipeBtn = QPushButton('+', self)
        self.addRecipeBtn.setToolTip("Добавьте рецепт")
        self.addRecipeBtn.resize(100, 30)
        self.addRecipeBtn.move(120, 50)

        self.addRecipeBtn.clicked.connect(self.addRecipe)

    def addRecipe(self):
        self.hide()
        self.addRecipeForm.show()