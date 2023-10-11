import mysql.connector

import Pages as pg

# cur = con.connect_to_database()['cursor']

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

def Encrypt():
    pass

def Decrypt():
    pass

def SignIn(data):
    cur.execute(f"SELECT email, password FROM User WHERE email='{data['email']}'")
    info = cur.fetchone()

    if not info:
        print("No User Found")

    else:
        if data['password'] == info[1]:
            print("LOGGED IN!")
            pg.Home()
        else:
            print("INCORRECT")

def create_user(user_info):

    cur.execute("SELECT * FROM User")
    rows = cur.fetchall()
    
    user_exists = False

    for row in rows:
        if user_info['email'] == row[3]:
            user_exists = True

    # CHECK IF USER ALREADY EXISTS
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