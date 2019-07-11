# import random

print("GAME OF GREED")

round_score = 0
total_score = 0
current_round = 0

print('Hit (x) to exit.')

while current_round <= 10:

    current_round += 1
    print("What was you score?")
    add_score = input()
    round_score = int(round_score) + int(add_score)
    total_score = int(total_score) + int(round_score)
    print(f'Your current score is {total_score}')
    print("Do you want to (b)ank or (r)oll' again?")
    next_action = input()

    if next_action == "r":
        current_round += 1

    if next_action == "b":

        print(f'Your total score was: {total_score}')

else:
    print("Game Over. Bye.")

if __name__ == "__main__":
    # game_of_greed()
