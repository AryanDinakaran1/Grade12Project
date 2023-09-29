import mysql.connector

def connect_to_database():
    try:
        con = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="password",
            port=3306,         
            database="mydb"
        )

        cursor = con.cursor()

        return {
            'connection' : con,
            'cursor' : cursor
        }

    except:
        return 0