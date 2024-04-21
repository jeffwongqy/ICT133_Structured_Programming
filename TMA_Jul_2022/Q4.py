
# define the filename 
filename1 = "Bad Citizen-202209081930.txt"
filename2 = "Bad Citizen-202209091930.txt"
filename3 = "Monkey Goes East-202209081430.txt"
filename4 = "Monkey Goes East-202209091430.txt"

def decipher(filename):
    # split the text using the dash as a delimiter 
    textSplit = filename.split("-")
    # decipher the production title
    prod_title = textSplit[0]

    # decipher the performance time
    hours = textSplit[1][8:10]
    mins = textSplit[1][10:12]
    performance_time = hours + ":" + mins

    # decipher the performance date 
    year = textSplit[1][0:4]
    month = textSplit[1][4:6]
    date = textSplit[1][6:8]
    performance_date = year + "-" + month + "-" + date

    return (prod_title, performance_date, performance_time)


def readSeatingPlan(filename):
    # read the file 
    file = open(filename, 'r', encoding='utf-8-sig')
    # read all lines from the file
    lines = file.readlines()

    # create an empty dict to store the seating plan 
    dict_seatingPlan = dict()
    # read each line 
    for line in lines:
        # split the data into a list using command as the delimiter 
        splitText = line.strip().split(",")
        # check if the key is present in the dictionary seating plan
        # if not, create a new key-value pair 
        if splitText[0] not in dict_seatingPlan:
            # create an empty list to store the values of the seating plan
            val_list = list()
            # read each value in the seating plan and append it into the value list 
            for val in splitText[1]:
                val_list.append(val)
            # store a list of seating plan into a new key dictionary
            dict_seatingPlan[splitText[0]] = val_list
    return dict_seatingPlan

def showSeatingPlan(seatingPlan):
    # iterate through key-value pair to display the seating plan
    for key, val in seatingPlan.items():
        print("{}  {}".format(key, '   '.join(val)))

    # create a string representation of the seat numbers 
    num_index = "  "
    for i in range(len(val)):
        if i < 9:
            num_index += str(0) + str(i+1) + "  "
        else:
            num_index += str(i+1) + "  " 

# call the function to decipher the production title and performance datetime
prod1 = decipher(filename1)
prod2 = decipher(filename2)
prod3 = decipher(filename3)
prod4 = decipher(filename4)

# read the file of the seating plan for all current productions
prod1_seating_plan = readSeatingPlan(filename1)
prod2_seating_plan = readSeatingPlan(filename2)
prod3_seating_plan = readSeatingPlan(filename3)
prod4_seating_plan = readSeatingPlan(filename4)


while True:
    # display the main menu
    print("Main Menu - FR Productions")
    print("==================================================")
    print("1. " + prod1[0] + " @ " + prod1[1] + " " + prod1[2])
    print("2. " + prod2[0] + " @ " + prod2[1] + " " + prod2[2])
    print("3. " + prod3[0] + " @ " + prod3[1] + " " + prod3[2])
    print("4. " + prod4[0] + " @ " + prod4[1] + " " + prod4[2])
    print("X. Exit")

    # prompt the user for selection
    selection = input("Enter selection: ")
    print()

    if selection == "1":
        while True:
            # display the production title
            print("Production: " + prod1[0])
            # display the performance datetime
            print("Performance datetime: " + prod1[1] + " " + prod1[2])
            # display the seating plan 
            print("Seating plan:")
            showSeatingPlan(prod1_seating_plan)
            print()
        
            # display a sub-menu
            print("Sub-Menu:")
            print("1. Book Seats")
            print("2. Cancel Bookings")
            print("X. Back to Main Menu")
            option = input("Enter option: ")
    
            if option == "1":
                # prompt the user to enter the seats to book
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and occupied seats
                count_block = 0
                count_occupied = 0
            
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod1_seating_plan.keys():
                        status = prod1_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been occupied, if yes, increment by 1
                    elif status == 'X':
                        print("Exception!! {} is BOOKED".format(book_seat))
                        count_occupied +=1
            
                # if both seats has been occupied or blocked, abort the booking system
                if count_block > 0 or count_occupied > 0:
                    print("This booking is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod1_seating_plan.keys():
                            prod1_seating_plan[key][seat_val-1] = 'X'

                    # display a message that booking has been done
                    print("Booking of {} done".format(book_seats_lists))
                    print()
                
            elif option == '2':
                # prompt the user to enter the seats to cancel
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and unoccupied seats
                count_block = 0
                count_unoccupied = 0
                
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod1_seating_plan.keys():
                        status = prod1_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been unoccupied, if yes, increment by 1
                    elif status == 'O':
                        print("Exception!! {} is not booked".format(book_seat))
                        count_unoccupied +=1
            
                # if both seats has been unoccupied or blocked, abort the cancellation system
                if count_block > 0 or count_unoccupied > 0:
                    print("This cancellation is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod1_seating_plan.keys():
                            prod1_seating_plan[key][seat_val-1] = 'O'

                    # display a message that booking has been done
                    print("Cancellation of booking for {} done".format(book_seats_lists))
                    print()
                
            elif option == 'X':
                break
    elif selection == "2":
        while True:
            # display the production title
            print("Production: " + prod2[0])
            # display the performance datetime
            print("Performance datetime: " + prod2[1] + " " + prod2[2])
            # display the seating plan 
            print("Seating plan:")
            showSeatingPlan(prod2_seating_plan)
            print()
        
            # display a sub-menu
            print("Sub-Menu:")
            print("1. Book Seats")
            print("2. Cancel Bookings")
            print("X. Back to Main Menu")
            option = input("Enter option: ")
    
            if option == "1":
                # prompt the user to enter the seats to book
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and occupied seats
                count_block = 0
                count_occupied = 0
            
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod2_seating_plan.keys():
                        status = prod2_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been occupied, if yes, increment by 1
                    elif status == 'X':
                        print("Exception!! {} is BOOKED".format(book_seat))
                        count_occupied +=1
            
                # if both seats has been occupied or blocked, abort the booking system
                if count_block > 0 or count_occupied > 0:
                    print("This booking is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod2_seating_plan.keys():
                            prod2_seating_plan[key][seat_val-1] = 'X'

                    # display a message that booking has been done
                    print("Booking of {} done".format(book_seats_lists))
                    print()
                    
            elif option == '2':
                # prompt the user to enter the seats to cancel
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and unoccupied seats
                count_block = 0
                count_unoccupied = 0
                
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod2_seating_plan.keys():
                        status = prod2_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been unoccupied, if yes, increment by 1
                    elif status == 'O':
                        print("Exception!! {} is not booked".format(book_seat))
                        count_unoccupied +=1
            
                # if both seats has been unoccupied or blocked, abort the cancellation system
                if count_block > 0 or count_unoccupied > 0:
                    print("This cancellation is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod2_seating_plan.keys():
                            prod2_seating_plan[key][seat_val-1] = 'O'

                    # display a message that booking has been done
                    print("Cancellation of booking for {} done".format(book_seats_lists))
                    print()
                
            elif option == 'X':
                break
        
    elif selection == "3":
        while True:
            # display the production title
            print("Production: " + prod3[0])
            # display the performance datetime
            print("Performance datetime: " + prod3[1] + " " + prod3[2])
            # display the seating plan 
            print("Seating plan:")
            showSeatingPlan(prod3_seating_plan)
            print()
        
            # display a sub-menu
            print("Sub-Menu:")
            print("1. Book Seats")
            print("2. Cancel Bookings")
            print("X. Back to Main Menu")
            option = input("Enter option: ")
    
            if option == "1":
                # prompt the user to enter the seats to book
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and occupied seats
                count_block = 0
                count_occupied = 0
            
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod3_seating_plan.keys():
                        status = prod3_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been occupied, if yes, increment by 1
                    elif status == 'X':
                        print("Exception!! {} is BOOKED".format(book_seat))
                        count_occupied +=1
            
                # if both seats has been occupied or blocked, abort the booking system
                if count_block > 0 or count_occupied > 0:
                    print("This booking is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod3_seating_plan.keys():
                            prod3_seating_plan[key][seat_val-1] = 'X'

                    # display a message that booking has been done
                    print("Booking of {} done".format(book_seats_lists))
                    print()
                    
            elif option == "2":
                # prompt the user to enter the seats to cancel
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and unoccupied seats
                count_block = 0
                count_unoccupied = 0
                
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod3_seating_plan.keys():
                        status = prod3_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been unoccupied, if yes, increment by 1
                    elif status == 'O':
                        print("Exception!! {} is not booked".format(book_seat))
                        count_unoccupied +=1
            
                # if both seats has been unoccupied or blocked, abort the cancellation system
                if count_block > 0 or count_unoccupied > 0:
                    print("This cancellation is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod3_seating_plan.keys():
                            prod3_seating_plan[key][seat_val-1] = 'O'

                    # display a message that booking has been done
                    print("Cancellation of booking for {} done".format(book_seats_lists))
                    print()
                
            elif option == 'X':
                break
            
    elif selection == '4':
        while True:
            # display the production title
            print("Production: " + prod4[0])
            # display the performance datetime
            print("Performance datetime: " + prod4[1] + " " + prod4[2])
            # display the seating plan 
            print("Seating plan:")
            showSeatingPlan(prod4_seating_plan)
            print()
        
            # display a sub-menu
            print("Sub-Menu:")
            print("1. Book Seats")
            print("2. Cancel Bookings")
            print("X. Back to Main Menu")
            option = input("Enter option: ")
    
            if option == "1":
                # prompt the user to enter the seats to book
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and occupied seats
                count_block = 0
                count_occupied = 0
            
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod4_seating_plan.keys():
                        status = prod4_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been occupied, if yes, increment by 1
                    elif status == 'X':
                        print("Exception!! {} is BOOKED".format(book_seat))
                        count_occupied +=1
            
                # if both seats has been occupied or blocked, abort the booking system
                if count_block > 0 or count_occupied > 0:
                    print("This booking is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod4_seating_plan.keys():
                            prod4_seating_plan[key][seat_val-1] = 'X'

                    # display a message that booking has been done
                    print("Booking of {} done".format(book_seats_lists))
                    print()
                    
            elif option == '2':
                # prompt the user to enter the seats to cancel
                book_seats = input("Enter seats to book: ")
                # get a list of book seats 
                book_seats_lists = book_seats.split(",")
                
                # count the number of block and unoccupied seats
                count_block = 0
                count_unoccupied = 0
                
                for book_seat in book_seats_lists:
                    # get the row key
                    key = book_seat[0]
                    # get the row seat number
                    seat_val = int(book_seat[1:])
                    # check if the seating plan is in the dictionary
                    if key in prod4_seating_plan.keys():
                        status = prod4_seating_plan[key][seat_val-1]
                    # check if the seat has been blocked, if yes, increment by 1
                    if status == '#':
                        print("Exception!! {} is BLOCKED".format(book_seat))
                        count_block +=1
                    # check if the seat has been unoccupied, if yes, increment by 1
                    elif status == 'O':
                        print("Exception!! {} is not booked".format(book_seat))
                        count_unoccupied +=1
            
                # if both seats has been unoccupied or blocked, abort the cancellation system
                if count_block > 0 or count_unoccupied > 0:
                    print("This cancellation is aborted")
                    print()
                else: # continue with the booking system 
                    for book_seat in book_seats_lists:
                        key = book_seat[0]
                        seat_val = int(book_seat[1:])
                        if key in prod4_seating_plan.keys():
                            prod4_seating_plan[key][seat_val-1] = 'O'

                    # display a message that booking has been done
                    print("Cancellation of booking for {} done".format(book_seats_lists))
                    print()
                
            elif option == 'X':
                break
            print()
    elif selection == 'X':
        break
        
        
                
            
        
        
    
    
    
    