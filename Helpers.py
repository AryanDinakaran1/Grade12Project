import mysql.connector
import Pages as pg

cur = {}

try:
    con = mysql.connector.connect(
                host="localhost",
                user="root",       
                password="password",
                port=3306,         
                database="mydb"
            )
    
    cur = con.cursor()

except:
    print("ERROR CONNECTING TO DATABASE")

def SignIn(data):
    cur.execute(f"SELECT * FROM User WHERE email='{data['email']}'")
    info = cur.fetchone()
    
    if not info:
        print("No User Found")

    else:
        if data['password'] == info[2]:
            print("LOGGED IN!")
            pg.Home({
                "id" : int(info[0]),
                "name" : info[1],
                "password" : info[2],
                "email" : info[3],
                "age" : int(info[4]),
                "is_admin" : info[5],
            })

        else:
            print("INCORRECT")

def create_user(user_info):

    cur.execute("SELECT * FROM User")
    rows = cur.fetchall()
    
    user_exists = False

    for row in rows:
        if user_info['email'] == row[3]:
            user_exists = True

    if user_exists:
        print("USER ALREADY EXISTS\n")
        pg.Authentication()

    if rows == []:
        set_id = 1

    else:
        set_id = rows[len(rows)-1][0] + 1

    query = f"INSERT INTO User(id, name, password, email, age, is_admin) VALUES ({set_id},'{user_info['name']}','{user_info['password']}','{user_info['email']}',{user_info['age']},'{user_info['is_admin']}')"
    cur.execute(query)
    con.commit()

    print("CREATED A NEW USER")

def get_user_by_id(user_id):
    cur.execute(f"SELECT * FROM User WHERE id = {user_id}")
    user = cur.fetchone()

    return user

def search_movie(name):
    cur.execute(f"SELECT * FROM Movie WHERE movie_name LIKE '%{name}%' ORDER BY release_date ASC")
    movies = cur.fetchall()

    return movies

def get_movies():
    cur.execute(f"SELECT * FROM Movie")
    movies = cur.fetchall()

    return movies

def get_movie_by_id(id):
    cur.execute(f"SELECT * FROM Movie WHERE movie_id = {id}")
    movie = cur.fetchone()

    return movie

def get_movies_by_genre(genre):
    cur.execute(f"SELECT * FROM Movie WHERE genre = '{genre}'")
    movies = cur.fetchall()

    return movies

def book_ticket(user_info, movie, cost):

    cur.execute("SELECT * FROM Ticket")
    rows = cur.fetchall()

    id = 0

    tickets = []

    for row in rows:
        tickets.append(row)

    if tickets == [] or tickets == None:
        id = 1

    else:
        id = len(tickets) + 1

    try:
        cur.execute(f"INSERT INTO Ticket(id, user_id, movie_id, cost) VALUES ({id}, {user_info['id']}, {movie[0]}, {cost})")
        con.commit()

    except Exception as e:
        print(e)
        return False

    return True

def get_tickets_by_user_id(user_id):
    cur.execute(f"SELECT Ticket.id, Ticket.user_id, Ticket.movie_id, Ticket.cost FROM Ticket, User WHERE User.id = Ticket.user_id && User.id = {user_id['id']}")
    tickets = cur.fetchall()

    return tickets

def create_movie(user_info, movie_info):
    cur.execute("SELECT * FROM Movie")
    rows = cur.fetchall()

    id = 0

    movies = []

    for row in rows:
        movies.append(row)


    if movies == [] or movies == None:
        id = 1

    else:
        id = len(movies) + 1

    try:
        cur.execute(f"INSERT INTO Movie (movie_id, movie_name, genre, release_date, rating) VALUES ({id}, '{movie_info['name']}', '{movie_info['genre']}', '{movie_info['release_date']}', {movie_info['rating']})")
        con.commit()

    except Exception as e:
        print("Something Went Wrong", e)
        return False
    
    return True