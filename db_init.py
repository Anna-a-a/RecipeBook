import sqlite3


conn = sqlite3.connect('recipe_book.db')
cur = conn.cursor()

#Create users table and fill data
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INT PRIMARY KEY,
   login TEXT,
   password TEXT);
""")

cur.execute("""INSERT INTO users(user_id, login, password) 
   VALUES(1, 'Anna', 'qwerty1');""")

cur.execute("""INSERT INTO users(user_id, login, password) 
   VALUES(2, 'Elena', 'qwerty2');""")


#Create recipes table and fill data
cur.execute("""CREATE TABLE IF NOT EXISTS recipes(
   recipe_id INT PRIMARY KEY,
   name TEXT,
   description TEXT,
   user_id INT);
""")

cur.execute("""INSERT INTO recipes(recipe_id, name, description, user_id) 
   VALUES(1, 'Rice', 'Рис с овощами и курицей', 1);""")

cur.execute("""INSERT INTO recipes(recipe_id, name, description, user_id) 
   VALUES(2, 'Salat', 'Салат салатный', 1);""")


#Create ingredients table and fill data
cur.execute("""CREATE TABLE IF NOT EXISTS ingredients(
   ingredient_id INT PRIMARY KEY,
   name TEXT);
""")

cur.execute("""INSERT INTO ingredients(ingredient_id, name) 
   VALUES(1, 'Рис');""")

cur.execute("""INSERT INTO ingredients(ingredient_id, name) 
   VALUES(2, 'Мясо');""")

cur.execute("""INSERT INTO ingredients(ingredient_id, name) 
   VALUES(3, 'Помидор');""")


#Create ingredients to recipe reference table and fill data
cur.execute("""CREATE TABLE IF NOT EXISTS recipes_ingredients(
   recipe_id INT,
   ingredient_id INT);
""")

cur.execute("""INSERT INTO recipes_ingredients(recipe_id, ingredient_id) 
   VALUES(1, 1);""")

cur.execute("""INSERT INTO recipes_ingredients(recipe_id, ingredient_id) 
   VALUES(1, 2);""")

cur.execute("""INSERT INTO recipes_ingredients(recipe_id, ingredient_id) 
   VALUES(2, 3);""")

cur.execute("""INSERT INTO recipes_ingredients(recipe_id, ingredient_id) 
   VALUES(2, 2);""")


