import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QComboBox, QTextEdit, QListWidget
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

        self.recipeComboBox = QComboBox(self)
        self.recipeComboBox.resize(110, 28)
        self.recipeComboBox.move(10, 51)
        self.recipeComboBox.currentTextChanged.connect(self.on_recipe_combobox_changed)

        self.addRecipeBtn = QPushButton('+', self)
        self.addRecipeBtn.setToolTip("Добавьте рецепт")
        self.addRecipeBtn.resize(100, 30)
        self.addRecipeBtn.move(120, 50)

        self.addRecipeBtn.clicked.connect(self.addRecipe)

        self.descriptionTextEdit = QTextEdit(self)
        self.descriptionTextEdit.move(10, 100)
        self.descriptionTextEdit.resize(200, 100)

        self.ingredientsListWidged = QListWidget(self)
        self.ingredientsListWidged.resize(300, 120)
        self.ingredientsListWidged.move(10, 150)

    def on_recipe_combobox_changed(self, name):
        if name == "":
            return
        # find selected recipe
        selectedRecipe = list(filter(lambda recipe : recipe[0] == name,self.recipes))[0]
        name, recipeId, description = selectedRecipe

        # fill description
        self.descriptionTextEdit.setText(description)

        # add ingredients
        self.ingredientsListWidged.clear()
        firstRecipeIngredients = self.repository.getIngredientsByRecipeId(recipeId)
        for ingredient in firstRecipeIngredients:
            ingredientId, name = ingredient
            self.ingredientsListWidged.addItem(name)

    def addRecipe(self):
        self.hide()
        self.addRecipeForm.show()

    def initPage(self, login, userId):
        # get user's recipes
        self.recipes = self.repository.getRecipes(userId)
        self.addRecipeForm.repository = self.repository
        self.addRecipeForm.userId = userId
        self.userId = userId
        self.addRecipeForm.mainForm = self

        # fill recipes combobox
        for recipe in self.recipes:
            name, recipeId, description = recipe
            self.recipeComboBox.addItem(name)

        # fill main window title
        self.setWindowTitle(f"{login}'s: Recipe Book")

    def updatePage(self):
        self.recipes = self.repository.getRecipes(self.userId)

        self.recipeComboBox.clear()
        for recipe in self.recipes:
            name, recipeId, description = recipe
            self.recipeComboBox.addItem(name)

