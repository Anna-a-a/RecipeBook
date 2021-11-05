import sqlite3

class Repository():
    def isUserExists(self, login, password):
        con = sqlite3.connect('recipe_book.db')
        cur = con.cursor()

        # Проверка пользователя в базе
        cur.execute(f"SELECT count(*) FROM users WHERE login = '{login}' AND password = '{password}'")
        value = cur.fetchone()

        cur.close()
        con.close()
        if value[0] == 0:
            return False
        else:
            return True

    def getUserIdByLogin(self, login):
        con = sqlite3.connect('recipe_book.db')
        cur = con.cursor()

        cur.execute(f"SELECT user_id FROM users WHERE login ='{login}'")
        return cur.fetchone()[0]

    def getRecipeNames(self, userId):
        con = sqlite3.connect('recipe_book.db')
        cur = con.cursor()

        cur.execute(f"SELECT name FROM recipes WHERE user_id = {userId}")
        return cur.fetchall()





