import sqlite3

# Подключение к базе данных
connection = sqlite3.connect("not_telegram.db", timeout=10)  # Ждать 10 секунд при блокировке
cursor = connection.cursor()

# Создаем таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,    
    username TEXT NOT NULL,       
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance REAL NOT NULL
)
""")


cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")


for i in range(1, 11):
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (f'User{i}', f'example{i}@gmail.com', i * 10, 1000.0)
    )


cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")


cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
records = cursor.fetchall()


for record in records:
    username, email, age, balance = record
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# cursor.execute("DELETE FROM USERS")
connection.commit()
connection.close()
