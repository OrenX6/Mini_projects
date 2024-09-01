import tkinter
from turtle import Turtle, Screen
import random

"""
The default size of a Turtle object is 20 pixels, 
which is the equivalent of the ratio 1 when resizing the Turtle.

"""


screen = Screen()
screen.bgpic("racetrack.png")
screen.setup(width=500, height=400)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
is_race_on = False

# set the game/ set the turtles:
y = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, y)
    turtles.append(new_turtle)
    y += 40


if user_bet in colors:
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            rand_distance = random.randint(1, 10)
            turtle.forward(rand_distance)
            if turtle.xcor() > 230:
                winner_color = turtle.pencolor()
                if user_bet == winner_color:
                    print(f"You won.The {winner_color} turtle is the winner.")
                else:
                    print(f"You lose!.The {winner_color} turtle is the winner.")
                is_race_on = False
else:
    is_race_on = False
    print("Invalid input, please trt again")

screen.exitonclick()












