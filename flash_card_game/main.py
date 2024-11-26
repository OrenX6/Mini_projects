import random
from tkinter import *

import pandas as pd

# global variables and constants:

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Comic Sans MS"
rand_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:  # file doesn't exists.
    data = pd.read_csv("data/french_words.csv")  # Dataframe object
except pd.errors.EmptyDataError:  # file exists but no data inside
    data = pd.read_csv("data/french_words.csv")

# cards:
words = data.to_dict(orient="records")  # list object - the items are dictionaries
print(words)


# ---------------------------- FLASH CARD ------------------------------- #

def flip_card(current_card):
    """
    flip the card after three second to the back and show the english translation of the word
    :param current_card:
    """
    card_image.config(file='images/card_back.png')
    canvas.itemconfig(tagOrId="title", text="English", fill="white")
    canvas.itemconfig(tagOrId="word", text=current_card["English"], fill="white")


# ---------------------------- GENERATE RANDOM CARD ------------------------------- #

def display_rand_card(check_mark=False):
    """
    :param check_mark:

    generate random French word and display it on the front card.
    flip the card after 3 seconds and update the data if the card is known.
    """

    global timer, rand_card
    master.after_cancel(timer)  # cancel a particular schedule of a callback function identified with ID

    if check_mark:  # we know the word
        update_data()

    rand_card = random.choice(words)  # Dict object
    card_image.config(file='images/card_front.png')
    canvas.itemconfig(tagOrId="title", text="French", fill="black")
    canvas.itemconfig(tagOrId="word", text=rand_card["French"], fill="black")
    timer = master.after(3000, flip_card, rand_card)  # flip the card (back card)


def update_data():
    """
    Update the words list and data file if the word is known.
    Create a new file words_to_learn if it's our first time to open the project.
    """
    # global is not required for mutable objects !
    words.remove(rand_card)  # update word lists
    new_data = pd.DataFrame(data=words)
    new_data.to_csv('data/words_to_learn.csv', index=False)  # update th


# ---------------------------- UI SETUP ------------------------------- #

master = Tk()  # root window
master.title("Flash Cards")
master.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = master.after(0, func=display_rand_card)  # set timer --> return None Type (immutable)

# Canvas:
canvas = Canvas(master, width=800, height=526)  # Construct a canvas widget object
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# image item:
card_image = PhotoImage()  # PhotoImage object 800 x 526
canvas.create_image(400, 263, image=card_image)  # Create image item with coordinates x1,y1.

# text item
canvas.create_text((400, 100), font=(FONT_NAME, 40, "bold"), tags="title")  # place a text
canvas.create_text((400, 263), font=(FONT_NAME, 60, "bold"), tags="word")

canvas.grid(columnspan=2)

# Buttons:
right_image = PhotoImage(file="images/right.png")
right_button = Button(master, image=right_image, bd=0, command=lambda: display_rand_card(check_mark=True))  # event
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(master, image=wrong_image, bd=0, command=display_rand_card)  # event
wrong_button.grid(row=1, column=0)

master.mainloop()
