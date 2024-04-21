import random

def getShape():
     # prompt the user to input a shape
    shape = input("please select a shape: ")
    
    # iteratively loop until a valid shape is entered
    while True:
        if shape.upper() != 'SCISSORS' and shape.upper() != 'PAPER' and shape.upper() != 'STONE':
            # display an error message for incorrect input shape
            print("Sorry, please select from Scissors, Paper, Stone")
            # prompt the user to input a shape again
            shape = input("please select a shape: ")
        else:
            break # exit the loop if input shape is valid
    return shape.upper()

def getRandomShape():
    # randomly select a shape 
    random_pick = random.choice(['SCISSORS', 'PAPER', 'STONE'])
    return random_pick

# prompt the user for player name 
player_name = input("Enter player's name: ")

while True:
    # initialize the player score and computer score to zero
    player_score = 0
    computer_score = 0

    # start the game 
    for i in range(3):
        # ask player to select a shape
        print("Round {}: {}".format(i+1, player_name))
        player_shape = getShape()
        # computer will randomly pick a shape
        computer_shape = getRandomShape()
        print("Round {}: Computer's shape is: {}".format(i+1, computer_shape))
        
        # award one point to the player  
        if (player_shape == "SCISSORS" and computer_shape == "PAPER") or (player_shape == "PAPER" and computer_shape == "STONE") or (player_shape == "STONE" and computer_shape == "SCISSORS"):
            player_score+=1
        # award one point to the computer
        elif (player_shape == "PAPER" and computer_shape == "SCISSORS") or (player_shape == "STONE" and computer_shape == "PAPER") or (player_shape == "SCISSORS" and computer_shape == "STONE"):
            computer_score+=1
        # display both computer score and player score for each round
        print("<< {} {} : Computer {} >>".format(player_name, player_score, computer_score))

    # if the player score is higher than the computer score, it ends the game
    if player_score > computer_score:
        print("{} is the winner!!".format(player_name))
        break
    elif computer_score > player_score: # if the computer score is higher than the player score, it ends the game
        print("Computer is the winner!!")
        break
    else:
        # if the result is a tie after 3 rounds, repeat the game again
        print("It's a tie!! Rematch...")
        continue