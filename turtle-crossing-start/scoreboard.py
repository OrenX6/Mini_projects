from turtle import Turtle

FONT = ("Courier", 24, "normal")  # global constant variable


class Scoreboard(Turtle):
    """
    A class to represent a scoreboard, write and update the level on screen
    also write the GAME OVER sequence when the game is over.
    ----------
    level : int
        Initial level of the game
    """

    def __init__(self):  # override

        """
        The constructor for Scoreboard class/Constructs all the necessary attributes for the Scoreboard object
        initialize the Scoreboard on the screen

        """

        super().__init__()  # access/call the init method from Turtle class
        self.level = 1  # default instance attribute
        self.hideturtle()  # method that belongs to Turtle class
        self.penup()
        self.setposition(-280, 260)
        self.display_level()

    def display_level(self):
        """
        delete the current level on the screen and update the new one
        """

        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def display_game_over(self):
        """
        display the GAME OVER on the screen
        """
        self.home()
        self.write(arg="GAME OVER !", align="center", font=FONT)

    def increase_level(self):
        """
        increase the level attribute by one
        """
        self.level += 1
        self.display_level()
