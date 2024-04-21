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

# initialize the player score and computer score to zero
player_score = 0
computer_score = 0
# initialize the index round to one
index = 1

# start the game 
while True:
    # prompt the player to select a shape
    print("Round {}: {}".format(index, player_name))
    player_shape = getShape()
    # computer will randomly pick a shape 
    computer_shape = getRandomShape()
    print("Round {}: Computer's shape is: {}".format(index, computer_shape))
    
    # compare the player shape against the computer pick
    if (player_shape == "SCISSORS" and computer_shape == "PAPER") or (player_shape == "PAPER" and computer_shape == "STONE") or (player_shape == "STONE" and computer_shape == "SCISSORS"):
        # award one point to the winner
        player_score+=1
        # reset the loser score to zero 
        computer_score = 0
    elif (player_shape == "PAPER" and computer_shape == "SCISSORS") or (player_shape == "STONE" and computer_shape == "PAPER") or (player_shape == "SCISSORS" and computer_shape == "STONE"):
        # reset the loser score to zero
        player_score = 0
        # award one point to the winner
        computer_score+=1
    else:
        # for a tie, reset both player and computer score to zero
        player_score = 0
        computer_score = 0 
    # display both player and computer score for each round
    print("<< {} {} : Computer {} >>".format(player_name, player_score, computer_score))

    # if a player wins 3 consecutive rounds will terminate the game
    if player_score == 3:
        print("{} is the winner after {} rounds!!".format(player_name, index))
        break
    elif computer_score == 3:
        print("Computer is the winner after {} rounds!!".format(index))
        break
    
    # if none of the player reaches 3 consecutive rounds, it will repeat the round until a player reaches 3 points
    index+=1