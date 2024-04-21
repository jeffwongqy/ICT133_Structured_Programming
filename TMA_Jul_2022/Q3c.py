import random 

def getHandOfShapes(size, auto):
    # initialize an empty list 
    shape_list = list()

    # initialize the number of scissors, paper, stone for player to zero 
    count_scissors_player = 0
    count_paper_player = 0
    count_stone_player = 0

    if auto == True:
        while True:
            # initialize the number of scissors, paper, stone for computer to zero
            count_scissors_computer = 0
            count_paper_computer = 0
            count_stone_computer = 0

            # shapes are randomly selected based on input size 
            for _ in range(size):
                shape = random.choice(['SCISSORS', 'PAPER', 'STONE'])
                # store the shape into a defined list
                shape_list.append(shape)
            if size > 1:
                # count the number of input scissors, paper, stone, respectively
                for shape_input in shape_list:
                    if shape_input == 'SCISSORS':
                        count_scissors_computer+=1
                    elif shape_input == 'PAPER':
                        count_paper_computer+=1
                    elif shape_input == 'STONE':
                        count_stone_computer+=1
                
                # compute the n shapes
                n_shape = size/2

                if count_scissors_computer > int(n_shape) or count_paper_computer > int(n_shape) or count_stone_computer > int(n_shape):
                    # initialize an empty list 
                    shape_list = list()
                    continue
                else:
                    break
            else:
                break
    else:
        for i in range(size):
            # prompt the player to indicate the shapes in sequential order
            shape = input("Shape {}: please select a shape: ".format(i+1))
            
            # count the number of input scissors, paper, stone, respectively
            if shape.upper() == 'SCISSORS':
                count_scissors_player+=1
            elif shape.upper() == 'PAPER':
                count_paper_player+=1
            elif shape.upper() == 'STONE':
                count_stone_player+=1
            
            # compute the n shapes 
            n_shape = size/2 
            
            # check that there should not be more than n/2 of the same shapes, respectively
            while True:
                if count_scissors_player > int(n_shape):
                    # display an error message
                    print("Cannot have more than {} SCISSORS!!".format(int(n_shape)))
                    # prompt the player to indicate the shapes in sequential order
                    shape = input("Shape {}: please select a shape: ".format(i+1))
                    if shape.upper() == 'SCISSORS':
                        continue
                    else:
                        count_scissors_player-=1
                        break
                elif count_paper_player > int(n_shape):
                    # display an error message
                    print("Cannot have more than {} PAPER!!".format(int(n_shape)))
                    # prompt the player to indicate the shapes in sequential order
                    shape = input("Shape {}: please select a shape: ".format(i+1))
                    if shape.upper() == "PAPER":
                        continue
                    else:
                        count_paper_player-=1
                        break
                elif count_stone_player > int(n_shape):
                    # display an error message
                    print("Cannot have more than {} STONE!!".format(int(n_shape)))
                    # prompt the player to indicate the shapes in sequential order
                    shape = input("Shape {}: please select a shape: ".format(i+1))
                    if shape.upper() == "STONE":
                        continue
                    else:
                        count_stone_player-=1
                        break
                else:
                    break
            # store the shape into a defined list
            shape_list.append(shape.upper())
    return shape_list


# initialize the computer score and player score to zero
computer_score = 0
player_score = 0

# prompt for the size of hand 
size = int(input("Enter size of hand: "))

# validate the size of hand
while True:
    if size < 3:
        # display an error message
        print("Size of hand must be at least 3")
        # prompt the user for size of hand
        size = int(input("Enter size of hand: "))
    else:
        break

# prompt for player name 
player_name = input("Enter player's name: ")

# setup the player hand of shapes according to the input size 
player_shape_list = getHandOfShapes(size, False)
# setup the computer hand of shapes according to the input size 
computer_shape_list = getHandOfShapes(size, True)

print()
print("Game starts...")
# iterate through both player shape list and computer shape list 
for i in range(size):
    print("Round {}: {} {}  :  Computer {}".format(i+1, player_name, player_shape_list[i], computer_shape_list[i]))

    # compare the computer and players hand of shapes
    # award one point to the player score
    if player_shape_list[i] == 'SCISSORS' and computer_shape_list[i] == 'PAPER':
        player_score+=1
    elif player_shape_list[i] == 'PAPER' and computer_shape_list[i] == 'STONE':
        player_score+=1
    elif player_shape_list[i] == 'STONE' and computer_shape_list[i] == 'SCISSORS':
        player_score+=1

    # award one point to the computer score 
    if computer_shape_list[i] == 'SCISSORS' and player_shape_list[i] == 'PAPER':
        computer_score+=1
    elif computer_shape_list[i] == 'PAPER' and player_shape_list[i] == 'STONE':
        computer_score+=1
    elif computer_shape_list[i] == 'STONE' and player_shape_list[i] == 'SCISSORS':
        computer_score+=1

    # display the score for each round of game
    print("<< {} {}  :  Computer {} >>".format(player_name, player_score, computer_score))
    if i != size-1:
        # prompt the user to press enter to proceed the current game
        input("Press <Enter> to proceed")
    print()
    
# check if the result is a tie 
if player_score > computer_score:
    # declare the player as winner
    print("{} is the winner!!".format(player_name))
elif computer_score > player_score:
    # declare the computer as winner
    print("Computer is the winner!!")
else:
    # display a message
    print("It's a tie!! Rematch...")
    print()

    # entering into playoff mode 
    while True:
        # initialize the index to zero
        index = 1

        # prompt the player to select a shape 
        playoff_player_shape = input("Playoff {}: {}, please select a shape: ".format(index, player_name))
        # setup the computer hand of shapes
        playoff_computer_shape = getHandOfShapes(1, True)
        # display the computer hand of shapes
        print("Playoff {}: Computer's shape is: {}".format(index, playoff_computer_shape[0]))
        
        # compare the computer and players hand of shapes
        # award one point to the player score
        if playoff_player_shape.upper() == 'SCISSORS' and playoff_computer_shape[0] == 'PAPER':
            player_score+=1
        elif playoff_player_shape.upper() == 'PAPER' and playoff_computer_shape[0] == 'STONE':
            player_score+=1
        elif playoff_player_shape.upper() == 'STONE' and playoff_computer_shape[0] == 'SCISSORS':
            player_score+=1

        # award one point to the computer score 
        if playoff_computer_shape[0] == 'SCISSORS' and playoff_player_shape.upper() == 'PAPER':
            computer_score+=1
        elif playoff_computer_shape[0] == 'PAPER' and playoff_player_shape.upper() == 'STONE':
            computer_score+=1
        elif playoff_computer_shape[0] == 'STONE' and playoff_player_shape.upper() == 'SCISSORS':
            computer_score+=1
        
        # check if the result is a tie 
        if player_score > computer_score:
            # declare the player as winner
            print("{} is the winner!!".format(player_name))
            break # end the game
        elif computer_score > player_score:
            # declare the computer as winner
            print("Computer is the winner!!")
            break # end the game
        else:
            # display a message
            print()
            index+=1
            continue
        

            









