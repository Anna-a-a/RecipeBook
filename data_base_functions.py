from PyQt5 import QtWidgets, QtCore, QtGui
from db_handler import *

class DataBase():
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


