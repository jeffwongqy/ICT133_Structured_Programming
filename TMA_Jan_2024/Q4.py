
bid_list = []

# display menu
print("<< COE Menu >>")
print("1. Submit/ Update bid")
print("2. Remove bid")
print("3. List bids")
print("4. Simulate allocation")
print("0. Quit")

while True:
    count_existing = 0
    # prompt the user for option
    option = int(input("Enter option: "))

    if option == 1:
        # prompt the user for identification 
        id = input("Enter bidder identification: ")
        
        # count the presence of bid corresponding to the id 
        for i in range(len(bid_list)):
            if id in bid_list[i]:
                count_existing+=1
        
        # check if the ID exists in the list of bids 
        if count_existing == 0:
            # prompt the user for reserve price
            reserve_price = int(input("Enter reserve price: "))
            # store the id and reserve price into list
            bid_list.append([id, reserve_price])
            # display message
            print("Your bid is submitted...")
            print()
        else:
            for i in range(len(bid_list)):
                if id in bid_list[i]:
                    # display the current reserve price
                    current_reserve_price = bid_list[i][1]
                    print("Your current reserve price is ${:.2f}".format(current_reserve_price))

                    # prompt the user for new reserve price
                    new_reserve_price = int(input("Enter new reserve price: "))

                    # update the new reserve price into existing id 
                    bid_list[i][1] = new_reserve_price

                    # display message
                    print("Your bid is updated...")
                    print()

    elif option == 2:
        count_existing = 0

        # prompt the user for identification 
        id = input("Enter bidder id to remove: ")
        
        # count the presence of bid corresponding to the id 
        for i in range(len(bid_list)):
            if id in bid_list[i]:
                count_existing+=1
        
        if count_existing == 0:
            print("No such bidder...")
            print()
        else:
            for i in range(len(bid_list)):
                if id in bid_list[i]:
                    # display the current reserve price
                    current_reserve_price = bid_list[i][1]
                    print("Your current reserve price is ${:.2f}".format(current_reserve_price))
                    # prompt the user to confirm remove
                    confirm_remove = input("Confirm remove? (Y/N): ")
                    if confirm_remove.upper() == 'Y':
                        # remove the bid from the bid list
                        del bid_list[i]
                        # display message
                        print("Bids remove successfully")
                        print()
                     
    elif option == 3:
        # count the number of bids in the list
        num_of_bids = len(bid_list)
        # display the total number of bids 
        print("Total number of bids received: {}".format(num_of_bids))
        # display all the submitted bids
        for i in range(num_of_bids):
            print("{}\t ${:.2f}".format(bid_list[i][0], bid_list[i][1]))
        print()
    
    elif option == 4:
        quota = input("Enter available COE (quota): ")

        if quota.isnumeric():
            # create a copy of bidder list
            bid_list_copy = bid_list
            # sort the bidders with highest reserve price to lowest reserve price using bubble sort
            for i in range(len(bid_list_copy) - 1):
                for j in range(len(bid_list_copy) - i - 1):
                    if bid_list_copy[j][1] < bid_list_copy[j+1][1]:
                        bid_list_copy[j], bid_list_copy[j+1] = bid_list_copy[j+1], bid_list_copy[j]
            # extract the list of available quota 
            available_quota = bid_list_copy[:int(quota)]
            # extract the COE price based on last successful bidders reserve price
            coe_price = available_quota[-1][1]
            # display the list of available quota
            for i in range(len(available_quota)):
                print("{} - Reserve Price ${:.2f} - COE ${:.2f}".format(available_quota[i][0], available_quota[i][1], coe_price))
            print()
        else:
            continue

    elif option == 0:
        break