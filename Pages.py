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
    pass

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

def Home():
    Authentication()

if __name__ == '__main__':
    Home()