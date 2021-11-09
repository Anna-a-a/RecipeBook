import sqlite3

class Repository():
    def __init__(self):
        self.dbName = 'recipe_book.db'

    def isUserExists(self, login, password):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()
        try:
            cur.execute(f"SELECT count(*) FROM users WHERE login = '{login}' AND password = '{password}'")
            value = cur.fetchone()
            if value[0] == 0:
                return False
            else:
                return True
        finally:
            cur.close()
            con.close()

    def addUser(self, user_id, login, password):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        try:
            cur.execute(f"INSERT OR IGNORE INTO users(user_id, login, password) "
                        f"VALUES({user_id}, '{login}', '{password}');")

        finally:
            con.commit()
            cur.close()
            con.close()

    def getUserIdByLogin(self, login):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()
        try:
            cur.execute(f"SELECT user_id FROM users WHERE login ='{login}'")
            return cur.fetchone()[0]
        finally:
            cur.close()
            con.close()


    def getRecipes(self, userId):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()
        try:
            cur.execute(f"SELECT name, recipe_id, description FROM recipes WHERE user_id = {userId}")
            return cur.fetchall()
        finally:
            cur.close()
            con.close()


    def getIngredientsByRecipeId(self, recipeId):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        try:
            cur.execute(f"SELECT i.ingredient_id, i.name from ingredients i "
                    f"JOIN recipes_ingredients ri ON i.ingredient_id = ri.ingredient_id "
                    f"WHERE ri.recipe_id = {recipeId}")
            return cur.fetchall()
        finally:
            cur.close()
            con.close()

    def addRecipe(self, recipe_id, name, description, user_id):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        try:
            cur.execute(f"INSERT INTO recipes(recipe_id, name, description, user_id)"
                        f" VALUES({recipe_id}, '{name}', '{description}', {user_id});")
        finally:
            con.commit()
            cur.close()
            con.close()

    def addIngredients(self, recipe_id, ingredient_id, name):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        try:
            cur.execute(f"INSERT OR IGNORE INTO ingredients(ingredient_id, name) "
                        f"VALUES({ingredient_id}, '{name}');")

            cur.execute(f"INSERT INTO recipes_ingredients(recipe_id, ingredient_id) "
                        f"VALUES({recipe_id}, {ingredient_id});")

        finally:
            con.commit()
            cur.close()
            con.close()

    def getIngredientsMaxId(self):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        try:
            cur.execute(f"SELECT MAX(ingredient_id) FROM ingredients")
            return cur.fetchone()

        finally:
            cur.close()
            con.close()

    def getRecipesMaxId(self):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()
        try:
            cur.execute(f"SELECT MAX(recipe_id) FROM recipes")
            return cur.fetchone()
        finally:
            cur.close()
            con.close()

    def getUsersMaxId(self):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()
        try:
            cur.execute(f"SELECT MAX(user_id) FROM users")
            return cur.fetchone()
        finally:
            cur.close()
            con.close()
