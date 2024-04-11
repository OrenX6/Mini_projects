import random
from art import stages, hangman
from hangman_words import word_list
import os


chosen_word = random.choice(word_list)
lives = 6
is_over = False
display = ["_" for _ in chosen_word]  # list comprehension

print(hangman)
print(chosen_word)

while not is_over:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose life.")

        if lives == 0:
            is_over = True
            print("You lose")

    print(" ".join(display))

    if "_" not in display:
        is_over = True
        print("You win !!")

    print(stages[lives])
