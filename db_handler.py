import sqlite3

def signIn(login, password, signal):
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    # Проверка пользователя в базе
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == password:
        signal.emit("Успешная авторизация!")
    else:
        signal.emit("Проверть правильность ввода данных!")

    cur.close()
    con.close()