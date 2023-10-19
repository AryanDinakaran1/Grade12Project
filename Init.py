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
conn = mysql.connector.connect(db_config)
cursor = conn.cursor()

# Create the Movies table
create_table_query = """
CREATE TABLE IF NOT EXISTS Movies (
    movie_id INT PRIMARY KEY,
    movie_name VARCHAR(255) NOT NULL,
    genre VARCHAR(255),
    release_date DATE,
    rating INT(10)
)
"""
cursor.execute(create_table_query)

# Insert movie records into the database
insert_query = "INSERT INTO Movies (movie_id, movie_name, genre, release_date, rating) VALUES (%s, %s, %s, %s, %s)"
for movie in movie_data:
    cursor.execute(insert_query, movie)

# Commit the changes and close the connection
conn.commit()
conn.close()