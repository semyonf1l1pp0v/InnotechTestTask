import sqlite3
import bcrypt

connection = sqlite3.connect("Users.db")
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS USERS')
connection.commit()

# Создаем таблицу

cursor.execute('''
CREATE TABLE IF NOT EXISTS USERS (
username text,
hashed_password text
)
''')
connection.commit()

cursor.execute('''
INSERT INTO USERS VALUES (?, ?)
''', ["admin", bcrypt.hashpw("admin".encode(), bcrypt.gensalt())])
connection.commit()

connection.close()
