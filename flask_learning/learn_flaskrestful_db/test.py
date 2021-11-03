import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

users = [
    (1, 'arun', 'asdf'),
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]
insert_query = "insert into users values (?, ?, ?)"
cursor.executemany(insert_query, users)

select_query = "select * from users"
for row in cursor.execute(select_query):
    print(row)
connection.commit()
