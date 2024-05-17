import sqlite3
import json

with open("C:/Users/emili/Documents/OOP/04-SQLite/Clase3DB/pixar_movies.json", "r") as file:
    pixar_movies = json.load(file)

conn = sqlite3.connect("pixar_movies.db")

# Crear tabla en de db y despuues se comenta
# conn.execute(""" 
# Create table if not exists movies (id integer primary key, title text not null,
#             year integer not null)
# """)

# Insertar los valores de un json en la tabla
#conn.executemany("INSERT INTO movies VALUES(:id, :title, :year)", pixar_movies)

cursor = conn.cursor()
# cursor.execute("SELECT * FROM movies")
# cursor.execute("SELECT * FROM movies WHERE year >= 2010")
# movies = cursor.fetchall()
# for movie in movies:
#     print(movie)

with open("C:/Users/emili/Documents/OOP/04-SQLite/Clase3DB/movie_viewers.json", "r") as file:
    movie_viewers = json.load(file)


# conn.execute("""
#               CREATE TABLE IF NOT EXISTS MovieViewers (
#               id INTEGER PRIMARY KEY,
#               movie_id INTEGER NOT NULL,
#               name TEXT NOT NULL,
#              last_name TEXT NOT NULL,
#              FOREIGN KEY (movie_id) REFERENCES Movies (id)
#               )
# """
# )

cursor.executemany("INSERT INTO MovieViewers Values(:id, :movie_id, :name, :last_name)", movie_viewers)

conn.commit()
conn.close()