from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from loginForm import *
from mainForm import *


class AddRecipeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("addRecipe.ui", self)
        self.initUI()

    def initUI(self):
        self.saveButton.clicked.connect(self.saveRecipe)
        self.addButton.clicked.connect(self.addIngredient)

    def addIngredient(self):
        countOfRecipes = self.repository.getRecipesMaxId()[0] + 1
        self.repository.addIngredients(countOfRecipes, self.repository.getIngredientsMaxId()[0] + 1,
                                       self.ingidientLineEdit.text())
        self.ingidientLineEdit.clear()

    def saveRecipe(self):
        countOfRecipes = self.repository.getRecipesMaxId()[0] + 1
        self.repository.addRecipe(countOfRecipes, self.nameEdit.text(), self.descriptionTextEdit.toPlainText(),
                                  self.userId)
        self.hide()
        self.mainForm.updatePage()
        self.mainForm.show()