from turtle import Screen, Turtle,TurtleScreen

import pandas as pd



screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

timmy = Turtle()
timmy.penup()
timmy.hideturtle()

data = pd.read_csv("50_states.csv")  # Dataframe object
print(data)
correct_guesses = []
score = 0

game_is_on = True

while score < 50:
    user_guess = screen.textinput(title=f"{score}/50 States Correct.", prompt="Enter state:")  # string

    if user_guess:
        user_guess = user_guess.title()

    if user_guess == "Exit":
        missing_states = [state for state in data.state if state not in correct_guesses]  # series object
        new_data = pd.Series(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_guess in data.state.values and user_guess not in correct_guesses:  # numpy ndarray
        row_state = data[data.state == user_guess]  # Dataframe object - select specific row
        x = row_state.x.item()  # Return the first element of the underlying data as a Python scalar.
        y = row_state.y.iloc[0]  # integer-location-based indexing of data in a DataFrame (attribute)

        timmy.goto((x, y))
        timmy.write(user_guess)
        correct_guesses.append(user_guess)
        score += 1

# Starts event loop
screen.mainloop()
