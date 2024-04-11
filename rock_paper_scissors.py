import art
import random

logos = [art.rock, art.paper, art.scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(logos[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")

    print(logos[computer_choice])

    outcome = ["It's a draw", "You win!", "You lose" ]
    print(outcome[user_choice - computer_choice])





