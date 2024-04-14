import random
# initialize the player 1 and player 2 scores to zero
player_1_scores = 0
player_2_scores = 0
# prompt the names representing the 2 players
player_1 = input("Enter player 1 name: ")
player_2 = input("Enter player 2 name: ")

# prompt the number rounds to play 
num_rounds = int(input("No of rounds to play: "))

for i in range(num_rounds):

    # randomly get the dice value for each player
    player_1_dice = random.randint(1, 6)
    player_2_dice = random.randint(1, 6)

    # display the players dice values 
    print("Round {} - {} {} : {} {}".format(i+1, player_1, player_1_dice, player_2, player_2_dice))

    # display the current score 
    if player_1_dice > player_2_dice:
        player_1_scores+=1
    elif player_2_dice > player_1_dice:
        player_2_scores+=1
    print("Current Score - {} {} : {} {}".format(player_1, player_1_scores, player_2, player_2_scores))
    print()

# declare the winner 
if player_1_scores > player_2_scores:
    print("{} is the winner!!".format(player_1))
elif player_2_scores > player_1_scores:
    print("{} is the winner!!".format(player_2))
else:
    print("It's a draw!!")
