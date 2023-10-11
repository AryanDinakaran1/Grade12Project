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
    name = input("Enter Movie Name: ")
    movies = hlp.search_movie(name)

    movies_data = []

    for id in range(len(movies)):

        movies_data.append({
            "id" : id+1,
            "name" : movies[id][2]
        })


    print("\nMovies: ")
    for movie in movies_data:
        print(f"{movie['id']}] {movie['name']}")
    print()

    movie_id = int(input("Enter Movie ID:"))
    MoviePage(movies_data[movie_id])

    

def MoviePage(data):
    pass


def Recommend():
    pass

def Home(user_info):

    if user_info['is_admin'] == "False":
        while True:
            print(f"Welcome, {user_info['name']}!")
            print("1] Book a Movie")
            print("2] Search a Movie")
            print("3] Recommend a Movie")
            print("4] Logout")
            print("5] EXIT")

            opt = int(input("Enter Option: "))
            
            if opt == 1:
                pass

            elif opt == 2:
                Search()

            elif opt == 3:
                pass

            elif opt == 4:
                Authentication()

            elif opt == 5:
                break

            else:
                print("WRONG INPUT")

    elif user_info['is_admin'] == "True":
        while True:
            print(f"Welcome, {user_info['name']}!")
            print("1] Movie Settings")
            print("2] Schedule Settings")
            print("3] Logout")
            print("4] EXIT")

            opt = int(input("Etner Option: "))
        

if __name__ == '__main__':
    Authentication()