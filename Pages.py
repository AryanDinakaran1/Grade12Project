import Helpers as hlp

def SignUp():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    age = int(input("Enter Age: "))
    password = input("Enter Password: ")

    data = {
        "name": name,
        "password": password,
        "email": email,
        "age": age,
        "is_admin": False
    }

    hlp.create_user(data)
    Home(data)

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

def Book(user_info):
    movies = hlp.get_movies()

    for movie in movies:
        print(f"{movie[0]}] {movie[1]}")

    opt = input("Choose Option: ")

    try:
        opt = int(opt)
    except:
        print("WRONG OPTION SELECTED")
        Home(user_info)

    Payment(user_info, opt)

def Payment(user_info, id):

    movie = ()
    try:

        movie = hlp.get_movie_by_id(id)

        if movie == None:
            print("No Movie Found")
            Book(user_info)

    except:
        print("Something Went Wrong... Try Agian!")
        Book(user_info)

    print(f"Name         : ", movie[1])
    print(f"Genre        : ", movie[2])
    print(f"Release Date : ", movie[3])
    print(f"Rating       : ", movie[4])

    print("1] Confirm Booking")
    print("2] Back to Movie Selection")
    print("3] Back to Home")

    opt = input("Choose Option: ")

    try:
        opt = int(opt)

    except:
        print("WRONG OPTION SELECTED")
        Payment(user_info, id)

    if opt == 1:
        Confirm(user_info, movie)
    elif opt == 2:
        Book(user_info)
    elif opt == 3:
        Home(user_info)
    else:
        print("WRONG OPTION SELECTED")
        Payment(user_info, id)

def Confirm(user_info, movie):
    print(f"Name         : ", movie[1])
    print(f"Genre        : ", movie[2])
    print(f"Release Date : ", movie[3])
    print(f"Rating       : ", movie[4])
    
    print("===============")

    ticketPrice = 200
    gst = (28/100)*ticketPrice

    print(f"Ticket Price: ₹{ticketPrice}")
    print(f"CGST: ₹{gst/2}")
    print(f"SGST: ₹{gst/2}")
    print(f"Total GST: ₹{gst}")

    print("===============")
    
    print(f"Final Cost: {ticketPrice+gst}")

    print("1] Book Ticket")
    print("2] Cancel Payment")

    opt = input("Choose an option: ")

    try:
        opt = int(opt)
    except:
        print("WRONG OPTION SELECTED")
        Confirm(user_info, movie)

    if opt == 1:

        try:

            is_booked = hlp.book_ticket(user_info, movie, (ticketPrice+gst))

            if is_booked:
                print("Ticket Booked... Enjoy your movie!")
                Home(user_info)
            else:
                print("Payment could not be processed")
                Confirm(user_info, movie)

        except Exception as e:
            print(e)
            Confirm(user_info, movie)

    elif opt == 2:
        Book(user_info)
    else:
        print("WRONG OPTION SELECTED")
        Confirm(user_info, movie)

def Search(data):
    name = input("Enter Movie Name: ")
    movies = hlp.search_movie(name)

    movies_data = []

    for id in range(len(movies)):

        movies_data.append({
            "id" : id+1,
            "name" : movies[id][1],
            "release_date" : movies[id][3],
            "genre" : movies[id][2],
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

def AddMovie(user_info):
    pass

def DeleteMovie(user_info):
    pass

def MovieSettings(user_info):

    while True:
        print("1] Add New Movie")
        print("2] Delete Movie")
        print("3] Back")

        opt = input("Enter Option: ")

        try:
            opt = int(opt)
        except:
            print("ERROR")

        if opt == 1:
            AddMovie(user_info)
        
        elif opt == 2:
            DeleteMovie(user_info)
        
        else:
            Home(user_info)

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
                Book(user_info)

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


