import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (f'User{i}', f'example{i}@gmail.com', i * 10, 1000.0)
    )

cursor.execute(''' 
UPDATE Users 
SET balance = 500 
WHERE id % 2 = 1
''')

cursor.execute("DELETE FROM Users WHERE id IN (1, 4, 7, 10)")

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

if total_users > 0:
    print(all_balances / total_users)
else:
    print(0)
# cursor.execute("DELETE FROM Users")
conn.commit()
conn.close()
