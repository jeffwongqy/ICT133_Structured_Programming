import random
# initialize the player 1 and player 2 scores to zero
player_1_scores = 0
player_2_scores = 0

# initialize the player 1 and player 2 consecutive rounds
player_1_wins_consecutive = 0
player_2_wins_consecutive = 0

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

    if player_1_dice == player_2_dice:
        player_1_wins_consecutive = 0
        player_2_wins_consecutive = 0
        player_1_scores = 0
        player_2_scores = 0
    elif player_1_dice > player_2_dice:
        player_1_scores += 1
        player_1_wins_consecutive += 1
    elif player_2_dice > player_1_dice:
        player_2_scores += 1
        player_2_wins_consecutive += 1
    
    print("Consecutive wins - {} {} : {} {}".format(player_1, player_1_scores, player_2, player_2_scores))

    if player_1_wins_consecutive == 2 or player_2_wins_consecutive == 2:
        break
    else:
        continue

# declare the winner 
if player_1_scores > player_2_scores:
    print("{} is the winner!!".format(player_1))
elif player_2_scores > player_1_scores:
    print("{} is the winner!!".format(player_2))
else:
    print("It's a draw!!")
