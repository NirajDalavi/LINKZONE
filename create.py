import sqlite3

connection=sqlite3.connect("users_data.db")
cursor=connection.cursor()
command="""CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""
# cursor.execute("INSERT INTO users VALUES ('db','1234567')")
# cursor.execute("INSERT INTO users VALUES ('saathvik','password-saat')")
# cursor.execute("INSERT INTO users VALUES ('aditya','password-raj')")
cursor.execute(command)
connection.commit()