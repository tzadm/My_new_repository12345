import sqlite3

connection_telegram_db = sqlite3.connect('not_telegram1.db')
cursor = connection_telegram_db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(ID INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(0, 10):
    cursor.execute(" INSERT INTO  Users (username, email, age, balance) VALUES ( ?, ?, ?, ?)",
                   (f'newuser{i + 1}', f'exemple{i + 1}@gmail.com', 10 * (i + 1), 1000))

cursor.execute('UPDATE Users SET balance = "500" WHERE id % 2 != 0 ')
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

cursor.execute('SELECT username, email, age, balance FROM Users GROUP BY age')
users = cursor.fetchall()
for user in users:
    if 60 in user:
        continue
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection_telegram_db.commit()
connection_telegram_db.close()
