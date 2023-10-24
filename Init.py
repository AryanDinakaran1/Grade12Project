import mysql.connector

# Replace with your own database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "mydb"
}

# Sample movie data
movie_data = [
    (1, 'The Shawshank Redemption', 'Drama', '1994-09-23', 4),
    (2, 'The Godfather', 'Crime', '1972-03-24', 5),
    (3, 'The Dark Knight', 'Action', '2008-07-18', 3),
    (4, 'Pulp Fiction', 'Crime', '1994-10-14', 2),
    (5, 'Forrest Gump', 'Drama', '1994-07-06', 3),
    (6, 'The Matrix', 'Science Fiction', '1999-03-31', 5),
    (7, 'The Lord of the Rings: The Return of the King', 'Fantasy', '2003-12-17', 3),
    (8, 'Inception', 'Science Fiction', '2010-07-16', 4),
    (9, 'Gladiator', 'Action', '2000-05-05', 4),
    (10, 'The Silence of the Lambs', 'Thriller', '1991-02-14', 2)
]

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydb"
)
cursor = conn.cursor()

# Create the Movies table
create_table_movie = """
CREATE TABLE IF NOT EXISTS Movie (
    movie_id INT PRIMARY KEY,
    movie_name VARCHAR(100),
    genre VARCHAR(100),
    release_date DATE,
    rating INT(10)
)
"""

create_table_user = """
CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    password VARCHAR(100),
    email VARCHAR(100),
    age INT(10),
    is_admin VARCHAR(100)
)
"""

create_table_ticket = """
CREATE TABLE IF NOT EXISTS Ticket (
    id INT PRIMARY KEY,
    user_id INT(10),
    movie_id INT(10),
    cost VARCHAR(100)
)
"""

create_table_actor = """
CREATE TABLE IF NOT EXISTS Actor (
    id INT PRIMARY KEY,
    name VARCHAR(100)
)
"""

cursor.execute(create_table_movie)
cursor.execute(create_table_user)
cursor.execute(create_table_ticket)
cursor.execute(create_table_actor)

# Insert movie records into the database
# create_admin = "INSERT INTO User (id, name, password, email, phone_num, age, is_admin) VALUES (1, 'Aryan Dinakaran', 'aryandinakaran@protonmail.com', 17, 'True')"
# cursor.execute(create_admin)

insert_query = "INSERT INTO Movie (movie_id, movie_name, genre, release_date, rating) VALUES (%s, %s, %s, %s, %s)"
for movie in movie_data:
    cursor.execute(insert_query, movie)

conn.commit()
conn.close()