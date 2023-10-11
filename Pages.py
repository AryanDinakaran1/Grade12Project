import Helpers as hlp

def SignUp():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone_num = int(input("Enter Phone Number: "))
    age = int(input("Enter Age: "))
    password = input("Enter Password: ")

    data = {
        "name": name,
        "password": password,
        "email": email,
        "phone_num": phone_num,
        "age": age,
        "is_admin": False
    }

    hlp.create_user(data)
    Home()

def SignIn():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    data = {
        'email' : email,
        'password' : password,
    }

    hlp.SignIn(data)

def Authentication():

    while True:
        print("1] Sign Up")
        print("2] Sign In")
        print("3] EXIT")

        opt = int(input("Choose Option Number: "))

        if opt == 1:
            SignUp()
        elif opt == 2:
            SignIn()
        elif opt == 3:
            break
        else:
            print("WRONG OPTION SELECTED\n")
            Authentication()

def Book():
    pass

def Search():
    pass

def Recommend():
    pass

def Home():
    while True:
        print("Welcome!")
        print("1] Book a Movie")
        print("2] Search a Movie")
        print("3] Recommend a Movie")
        print("4] Logout")
        print("5] EXIT")

        opt = input("Enter Option: ")

        if opt == 1:
            pass

        elif opt == 2:
            pass

        elif opt == 3:
            pass

        elif opt == 4:
            Authentication()

        elif opt == 5:
            break

        else:
            print("WRONG INPUT")

if __name__ == '__main__':
    Authentication()