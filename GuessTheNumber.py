from art import logo_Guss_The_Number
from random import randint
from os import system

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """
    ask the user for the difficulty level and return the turns correspondingly.
    :return: turns
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def compare(guess_number, answer):
    """
     Function to check user's guess against actual answer
    :param guess_number:
    :param answer:
    """
    if guess_number > answer:
        print("Too high")
    elif guess_number < answer:
        print("Too low")
    else:
        print(f"You got it!, the answer was {guess_number}.")


def game():
    print(logo_Guss_The_Number)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = randint(1, 101)
    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        compare(guess, number)

        if guess == number: 
            return
        turns -= 1
    else:
        print("You have run out of guesses, you lose.")


while input("Do you want to play a Number Guessing Game? Type 'y' or 'n': ").lower() == 'y':
    system('cls')
    game()
