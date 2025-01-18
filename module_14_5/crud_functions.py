import sqlite3


def initiate_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()

        # Создание таблицы Products
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            )
        ''')

        # Создание таблицы Users
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
            )
        ''')

        conn.commit()


def get_all_products():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        return cursor.fetchall()


def add_product(title, description, price):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (title, description, price))
        conn.commit()


def add_user(username, email, age):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)',
            (username, email, age)
        )
        conn.commit()


def is_included(username):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
        return cursor.fetchone() is not None
