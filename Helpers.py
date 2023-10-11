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
                "phone_num" : int(info[4]),
                "age" : int(info[5]),
                "is_admin" : info[6],
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

    query = f"INSERT INTO User(id, name, password, email, phone_num, age, is_admin) VALUES ({set_id},'{user_info['name']}','{user_info['password']}','{user_info['email']}',{user_info['phone_num']},{user_info['age']},'{user_info['is_admin']}')"
    cur.execute(query)
    con.commit()

    print("CREATED A NEW USER")

def search_movie(name):
    cur.execute(f"SELECT * FROM Movie WHERE name LIKE '%{name}%' ORDER BY release_date ASC")
    movies = cur.fetchall()

    return movies