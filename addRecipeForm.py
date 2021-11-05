from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from repository import *
from PyQt5 import uic
from mainForm import *


class AddRecipeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("addRecipe.ui", self)
        self.initUI()

    def initUI(self):
        pass