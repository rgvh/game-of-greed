import random
print("GAME OF GREED")
'''
Game of Greed objectives:
Application should simulate rolling between 1 and 6 dice
Application should allow user to set aside dice each roll
Application should user to enter score per roll
Application should allow “banking” current score or rolling again.
Application should keep track of total score
Application should keep track of current round
track:
current round
number of dice being rolled
score
'''
current_round = 1
round_score = 0
total_score = 0

play = input("Would you like to play?")
if play == 'y':

    if play == 'n':
        print("Sorry, you're missing out")

print(f'Starting round {current_round}')
set_aside = 0
roll = []


# def roll_dice(p)
# for i in range(set_aside, 6):
#     selected = random.randint(1, 6)
#     roll.append(selected)
# print(f'Your rolled: {roll}')
current_round += 1

# print("Which results do you wish to keep?")
# new_aside = input()
# set_aside = int(set_aside) + len(new_aside)
# print(f'You have currently are holding {set_aside} die aside')

print("What was you score?")
add_score = input()
round_score = int(round_score) + int(add_score)
total_score = int(total_score) + int(round_score)
print(f'Your current score is {total_score}')

print("Do you want to 'bank' or 'roll' again?")
# next actioninput()

print(f'Game Over.  Your total score was: {total_score}')
