import sys
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
            sys.exit(0)

        else:
            print("WRONG OPTION SELECTED\n")
            Authentication()

# def Book(user_info):
#     movies = hlp.get_movies()

#     for movie in movies:
#         print(f"{movie[0]}] {movie[1]}")

#     opt = input("Choose Option: ")

#     try:
#         opt = int(opt)
#     except:
#         print("WRONG OPTION SELECTED")
#         Home(user_info)

#     Payment(user_info, opt)

# def Payment(user_info, id):

#     movie = ()
#     try:

#         movie = hlp.get_movie_by_id(id)

#         if movie == None:
#             print("No Movie Found")
#             Book(user_info)

#     except:
#         print("Something Went Wrong... Try Agian!")
#         Book(user_info)

#     print(f"Name         : ", movie[1])
#     print(f"Genre        : ", movie[2])
#     print(f"Release Date : ", movie[3])
#     print(f"Rating       : ", movie[4])

#     print("1] Confirm Booking")
#     print("2] Back to Movie Selection")
#     print("3] Back to Home")

#     opt = input("Choose Option: ")

#     try:
#         opt = int(opt)

#     except:
#         print("WRONG OPTION SELECTED")
#         Payment(user_info, id)

#     if opt == 1:
#         Confirm(user_info, movie)
#     elif opt == 2:
#         Book(user_info)
#     elif opt == 3:
#         Home(user_info)
#     else:
#         print("WRONG OPTION SELECTED")
#         Payment(user_info, id)

# def Confirm(user_info, movie):
#     # Display movie information
#     print(f"Name         : ", movie[1])
#     print(f"Genre        : ", movie[2])
#     print(f"Release Date : ", movie[3])
#     print(f"Rating       : ", movie[4])
    
#     print("===============")

#     ticketPrice = 200
#     gst = (28/100)*ticketPrice

#     print(f"Ticket Price: ₹{ticketPrice}")
#     print(f"CGST: ₹{gst/2}")
#     print(f"SGST: ₹{gst/2}")
#     print(f"Total GST: ₹{gst}")

#     print("===============")
    
#     print(f"Final Cost: {ticketPrice+gst}")

#     print("1] Book Ticket")
#     print("2] Cancel Payment")

#     opt = input("Choose an option: ")

#     try:
#         opt = int(opt)

#     except ValueError:
#         print("WRONG OPTION SELECTED")
#         Confirm(user_info, movie)

#     if opt == 1:
#         try:
             
#             is_booked = hlp.book_ticket(user_info, movie, (ticketPrice + gst))

#             if is_booked:
#                 print("Ticket Booked... Enjoy your movie!")
#                 Home(user_info)
#             else:
#                 print("Payment could not be processed")
#                 Confirm(user_info, movie)

#         except Exception as e:
#             print(e)
#             Confirm(user_info, movie)

#     elif opt == 2:
#         # Assuming there's a function named Book
#         Book(user_info)
#     else:
#         print("WRONG OPTION SELECTED")
#         Confirm(user_info, movie)

def display_theater(seats):
    for row in seats:
        row_str = ""
        for seat in row:
            row_str += seat + " "
        print(row_str)

def select_seat(seats, row_num, seat_num):
    if seats[row_num][seat_num] == "✅":
        print("Sorry, this seat is already taken.")
    else:
        seats[row_num][seat_num] = "✅"
        print("Seat selected!")

def create_theater(rows, seats_per_row):
    theater = []
    for _ in range(rows):
        row = ["O"] * seats_per_row
        theater.append(row)
    return theater

def book_seats(num_tickets):
    rows = 5
    seats_per_row = 10
    theater_seats = create_theater(rows, seats_per_row)
    for _ in range(num_tickets):
        
        while True:
            display_theater(theater_seats)

            row_num = int(input(f"Enter the row number (0 to {rows - 1}): "))
            seat_num = int(input(f"Enter the seat number (0 to {seats_per_row - 1}): "))

            display_theater(theater_seats)

            if 0 <= row_num < rows and 0 <= seat_num < seats_per_row:
                select_seat(theater_seats, row_num, seat_num)
                break
            else:
                print("Invalid row or seat number. Please try again.")


def book_movie(user):
    print("Book Movie:")
    movie_id = input("Enter the Movie ID you want to book: ")
    movie = hlp.get_movie_by_id(movie_id)

    if not movie:
        print("Movie not found.")

    else:
        print(f"Selected Movie: {movie[1]}")
        showtimes = input("Enter the showtimes (comma-separated): ")
        num_tickets = int(input("Enter the number of tickets: "))
        book_seats(num_tickets)

        # Calculate the total price
        total_price = num_tickets * 200

        print("Total price: Rs. ", total_price)
        confirm = input("Confirm booking (yes/no): ").strip().lower()

        if confirm == "yes":
            is_booked = hlp.create_booking(user, movie, showtimes, num_tickets, total_price)

            if is_booked:
                Payment(total_price)

            else:
                print("Booking Failed")

        else:
            print("Booking canceled.")

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
    name = input("Enter Movie Name: ")
    genre = input("Enter Movie Genre: ")
    release_date = input("Enter Movie Release Date: ")
    rating = input("Enter Movie Rating: ")

    try:
        rating = int(rating)
    except:
        print("Rating Must be an Integer")
        AddMovie(user_info)

    if rating > 5:
        print("Rating cannot be more than 5")
        AddMovie(user_info)

    movie_info = {
        'name' : name,
        'genre' : genre,
        'release_date' : release_date,
        'rating' : rating
    }

    movie_added = hlp.create_movie(user_info, movie_info)

    if movie_added:
        print(f"Added Movie {name}")
    else:
        print(f"Could Not Add Movie {name}")
        AddMovie(user_info)

def DeleteMovie(user_info):
    movies = hlp.get_movies()

    for movie in movies:
        print(f"{movie[0]}] {movie[1]}")

    opt = input("Enter an Option: ")

    try:
        opt = int(opt)

        is_deleted = hlp.delete_movie_by_id(opt)

        if is_deleted:
            print("Movie Deleted")
            MovieSettings(user_info)
        else:
            print("Could not find movie")
            DeleteMovie(user_info)

    except:
        DeleteMovie(user_info)

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

def CancelTicket():
    pass

def Tickets(user_info):
    tickets = hlp.get_tickets_by_user_id(user_info)
    data = []

    for ticket in tickets:
        data.append({
            'id' : ticket[0],
            'user' : hlp.get_user_by_id(ticket[1]),
            'movie' : hlp.get_movie_by_id(ticket[2]),
            'cost' : ticket[3]
        })

    for row in data:
        print(f"{row['id']}] {row['movie'][1]} -> ₹{row['cost']}")

    print("\n==========\n")

    print("1] Cancel Ticket")
    print("2] Back to Home")

    opt = input("Enter Option: ")

    try:
        opt = int(opt)

    except:
        Tickets(user_info)

    if opt == 1:
        # CancelTicket(user_info, data)
        pass

    elif opt == 2:
        Home(user_info)

def Payment(cost):
    print('1] Payment by Credit/Debit Card')
    print('2] Payment by UPI')
    
    opt = int(input('Choose Option: '))

    if opt == 1:
        int(input('Enter Creditcard number: '))
        int(input('Enter CVV: '))
        print(f'Payment of ₹{cost} done successfully\n')

    if opt == 2:
        int(input('Enter UPI-id: '))
        int(input('Enter pin: '))
        print(f'Payment of ₹{cost} done successfully\n')


def Home(user_info):
    if user_info['is_admin'] == "False":
        while True:
            print(f"Welcome, {user_info['name']}!")
            print("1] Book a Movie")
            print("2] Search a Movie")
            print("3] My Tickets")
            print("4] Logout")
            print("5] EXIT")

            opt = input("Enter Option: ")

            try:
                opt = int(opt)

            except:
                print("\nWRONG OPTION SELECTED\n")
                Home(user_info)

            if opt == 1:
                book_movie(user_info)

            elif opt == 2:
                Search(user_info)

            elif opt == 3:
                Tickets(user_info)

            elif opt == 4:
                Authentication()

            elif opt == 5:
                sys.exit(0)

            else:
                print("WRONG INPUT")
                Home(user_info)

    elif user_info['is_admin'] == "True":
        
        while True:
            print(f"Welcome, {user_info['name']}!")
            print("1] Movie Settings")
            # print("2] Manage Admin")
            print("2] Logout")
            print("3] EXIT")

            opt = input("Enter Option: ")

            try:
                opt = int(opt)

            except:
                Home(user_info)

            if opt == 1:
                MovieSettings(user_info)

            # elif opt == 2:
            #     pass

            elif opt == 2:
                Authentication()

            elif opt == 3:
                sys.exit(0)

            else:
                print("WRONG OPTION SELECTED")
                Home(user_info)

if __name__ == '__main__':
    Authentication()
