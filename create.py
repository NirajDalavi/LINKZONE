import sqlite3

connection=sqlite3.connect("users_data.db")
cursor=connection.cursor()
command="""CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""

cursor.execute(command)
connection.commit()