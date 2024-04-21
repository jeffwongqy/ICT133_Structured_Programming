import random 

def getHandOfShapes(size, auto):
    # initialize an empty list 
    shape_list = list()

    if auto == True:
        # shapes are randomly selected based on input size 
        for _ in range(size):
            shape = random.choice(['SCISSORS', 'PAPER', 'STONE'])
            # store the shape into a defined list
            shape_list.append(shape)
    else:
        for i in range(size):
            # prompt the player to indicate the shapes in sequential order
            shape = input("Shape {}: please select a shape: ".format(i+1))
            # store the shape into a defined list
            shape_list.append(shape.upper())
    return shape_list

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

while True:
    # initialize the computer score and player score to zero
    computer_score = 0
    player_score = 0

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
        break # end the game 
    elif computer_score > player_score:
        # declare the computer as winner
        print("Computer is the winner!!")
        break # end the game 
    else:
        # display a message
        print("It's a tie!! Rematch...")
        print()
        continue





