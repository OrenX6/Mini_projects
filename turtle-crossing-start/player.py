from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):  # inherit all the methods and attributes from its parent class (Turtle)
    """
    The turtle which we are controlling to cross the road
    """

    def __init__(self):  # Default init constructor
        super().__init__()  # call/access the init method defined in the superclass (Turtle)
        self.shape("turtle")  # initialize the object’s attributes
        self.setheading(90)
        self.penup()
        self.reset_position()

    def go_up(self):
        """
        move the turtle forwards by specific distance
        """
        self.forward(MOVE_DISTANCE)

    def cross_finish_line(self):
        """
        check if the play cross the finish line or not
        :return: True or False
        """
        return self.ycor() >= FINISH_LINE_Y

    def collide_with(self, car):
        """
        Check if player collide with a specific car on the screen or not
        :param car: Turtle object
        :return: True or False
        """
        if abs(car.xcor() - self.xcor()) < 28 and abs(car.ycor() - self.ycor()) < 20:
            return True
        else:
            return False

    def reset_position(self):
        """
        move the turtle back to the original position (starting position)
        """
        self.goto(STARTING_POSITION)
