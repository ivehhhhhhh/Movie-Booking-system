movies=[
    {"id": 3001, "title": "Avengers: Endgame", "price": 15.00, "seats": 50},
    {"id": 3002, "title": "Inception", "price": 12.00, "seats": 30},
    {"id": 3003, "title": "Interstellar", "price": 14.00, "seats": 20},
    {"id": 3004, "title": "The Matrix", "price": 10.00, "seats": 0},
    {"id": 3005, "title": "Titanic", "price": 8.00, "seats": 10},
]

cost = 0
movies_booked = [] # {"movie_id_booked":"3001", "tickets_purchased": 1} (example)

def display_movies():
    print("\n")
    print("Available Movies:")
    print("|ID      |Title                           |   Price (RM) | Seats Available |")
    print("---------------------------------------------------------------------------")
    for movie in movies:
        print(f"| {movie['id']:<6} | {movie['title']:<30} | {movie['price']:>10.2f}   | {movie['seats']:>15} |")


#function to book ticktes
def book_tickets():
    try:
        movie_id=int(input("Enter movie ID>>"))
    except:
        print('Invalid input entered')
        return
    
    if(movie_id < 0):
        print('Movie ID must be positive')
        return

    isMovieFound = False
    
    for movie in movies:
        global cost
        if movie["id"]==movie_id:
            isMovieFound = True
            try:
                num_tickets=int(input("\nEnter number of tickets>>"))
            except:
                print('Invalid input entered')
                return
                        
            if(movie_id < 0):
                print('Movie ID must be positive')
                return
            
            if num_tickets <= movie["seats"]:
                movie["seats"] = movie["seats"]-num_tickets
                cost += num_tickets*movie["price"]
                
                # Add movie into movies_booked
                hasExistingBooking = False
                for booking in movies_booked:
                    # If the movie is already in the booked list, update the ticket count
                    if (booking["movie_id_booked"] == movie["id"]):
                        hasExistingBooking = True
                        booking["tickets_purchased"] += num_tickets
                # If it's a new booking, add it to the list
                if not hasExistingBooking:
                    movies_booked.append({"movie_id_booked": movie["id"], "tickets_purchased": num_tickets})
                
                print(f"Succesfully booked {num_tickets} tickets for {movie['title']}.")
                book_more_tickets()
                return
            else:
                print("Not enough seats available")
                choice()
    
    if not isMovieFound: 
        print('\nMovie ID Not Found :(\n')
        choice()
#if user choose to book more tickets
def book_more_tickets():
    more_tickets=input("Do you want to book more tickets (yes/no):")
    if more_tickets=="yes":
        display_movies()
        book_tickets()
        return
    else:
        print('\n Going back to main menu... \n')
        return
    
#function for cancelling tickets
def cancel_tickets():
    movie_id = int(input("Enter Movie ID to cancel tickets: "))

    for movie in movies:
        global cost
        if movie["id"] == movie_id:
            
            #  Check if user has purchased tickets
            num_tickets_bought = check_if_movies_booked(movie_id)
            if (num_tickets_bought < 0): 
                print('You did not purchase any tickets for this movie.\n')
                return
            
            num_tickets_cancelled = int(input("Enter number of tickets to cancel: "))
            
            # Check if num_tickets_cancelled > num_tickets_bought
            if (num_tickets_cancelled > num_tickets_bought):
                print('You can\'t cancel more tickets than you bought.\n')
                return
            
            num_tickets = num_tickets_bought - num_tickets_cancelled
            print(num_tickets)
            update_movies_booked_cancelled(movie_id, num_tickets) # update movies_booked when cancel tickets
            movie["seats"] = movie["seats"] + num_tickets_cancelled
            cost -= num_tickets_cancelled * movie["price"]
            print(f"Successfully canceled {num_tickets_cancelled} tickets for {movie['title']}.")
            return
    print("Movie ID not found.")

# Check if user has purchased tickets for given movie_id
# if yes: return number of tickets purchased
# if no: return -1
def check_if_movies_booked(movie_id):
    for booking in movies_booked:
        if booking["movie_id_booked"] == movie_id:
            return booking["tickets_purchased"]
    return -1

def update_movies_booked_cancelled(movie_id, updated_num_tickets):
    for booking in movies_booked:
        if booking["movie_id_booked"] == movie_id:
            booking["tickets_purchased"] = updated_num_tickets
            return
        
#exit the system and display price
def exit_system():
    global cost
    print("Thank you for using the Movie Ticket Booking System.") 
    print(f"Total price of tickets purchased: RM{cost:.2f}")
    exit()
    
#call the function based on user's choice
def choice():
    while True:
        display_movies()
        print("Choose an action: (1) Book Tickets, (2) Cancel Tickets, (3) Exit:")
        choice = int(input())
        
        if choice == 1:
            book_tickets()
        elif choice == 2:
            cancel_tickets()
        elif choice == 3:
            exit_system()
            break
        else:
            print("Invalid choice. Please try again.")
choice()
