import mysql.connector

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