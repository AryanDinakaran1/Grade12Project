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

        opt = input("Choose Option Number: ")

        try:
            opt = int(opt)

        except:
            print("WRONG OPTION SELECTED\n")
            Authentication()

        if opt == 1:
            SignUp()

        elif opt == 2:
            SignIn()

        elif opt == 3:
            print("EXIT WITH 0 ERRORS")
            break

        else:
            print("WRONG OPTION SELECTED\n")
            Authentication()

def Book():
    pass

def Search(data):
    name = input("Enter Movie Name: ")
    movies = hlp.search_movie(name)

    movies_data = []

    for id in range(len(movies)):

        movies_data.append({
            "id" : id+1,
            "name" : movies[id][2],
            "release_date" : movies[id][1],
            "genre" : movies[id][3],
            "rating" : movies[id][4],
        })

    if movies_data == []:
        print("\nNo Movie Found\n")
        Home(data)


    print("\nMovies: ")
    for movie in movies_data:
        print(f"{movie['id']}] {movie['name']}")
    print()

    movie_id = int(input("Enter Movie ID:"))
    MoviePage(movies_data[movie_id-1], data)

def MoviePage(data, user_info):
    print("Name: ", data["name"])
    print("Release Date: ", data["release_date"])
    print("Genre: ", data["genre"])
    print("Rating: ", data["rating"])

    print()

    print("1] Back to Searching")
    print("2] Back to Home")

    opt = int(input("Enter Option: "))

    if opt == 1:
        Search(user_info)
    elif opt == 2:
        Home(user_info)
    else:
        print("WRONG INPUT")
        MoviePage(data, user_info)

def MovieSettings(user_info):

    while True:
        print("1] Add New Movie")
        print("2] Delete Movie")
        print("3] Back")

def ScheduleSettings():
    pass

def ManageAdmin():
    pass

def Home(user_info):

    if user_info['is_admin'] == "False":
        while True:
            print(f"Welcome, {user_info['name']}!")
            print("1] Book a Movie")
            print("2] Search a Movie")
            print("3] Logout")
            print("4] EXIT")

            opt = input("Enter Option: ")

            try:
                opt = int(opt)
            except:
                print("\nWRONG OPTION SELECTED\n")
                Home(user_info)

            if opt == 1:
                Book()

            elif opt == 2:
                Search(user_info)

            elif opt == 3:
                Authentication()

            elif opt == 4:
                break

            else:
                print("WRONG INPUT")
                Home(user_info)

    elif user_info['is_admin'] == "True":
        while True:
            print(f"Welcome, {user_info['name']}!")
            print("1] Movie Settings")
            print("2] Schedule Settings")
            print("3] Manage Admin")
            print("4] Logout")
            print("5] EXIT")

            opt = int(input("Enter Option: "))

if __name__ == '__main__':
    Authentication()