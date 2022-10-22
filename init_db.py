import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO jogos (nome, categoria, console) VALUES (?, ?, ?)",
            ('Mario Kart', 'RPG', 'XBOX' )
            )

cur.execute("INSERT INTO jogos (nome, categoria, console) VALUES (?, ?, ?)",
            ('League Of Legends', 'RPG', 'PC' )
            )

cur.execute("INSERT INTO jogos (nome, categoria, console) VALUES (?, ?, ?)",
            ('Mobile Legends', 'RPG', 'PC' )
            )

cur.execute("INSERT INTO usuarios (nome, nickname, senha) VALUES (?, ?, ?)",
            ('Elza', 'Elza', 'Elza' )
            )
connection.commit()
connection.close()