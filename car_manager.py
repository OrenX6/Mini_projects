import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

"""
The reason the CarManager does not inherit from the Turtle class is because the CarManager 
instance that we create does not need the behaviors or attributes of Turtle. We don't tell 
the CarManager object to goto a place on the screen, or move forward, change color, change shape, 
write, set a heading, etc. The CarManager object is not a turtle that appears on the screen. 
It's a utility for creating and maintaining a list of cars, which are turtles, 
and performing actions on those turtles that it created, that's all.


keeps generating cars can have not only memory issue, but also calculating the collision will
takes longer time as you keep staying in the game. This cause some bugs mentioned in other questions
that in high levels the car run though the turtle but not game over.
"""



class CarManager:
    """
    Generate random cars on the screen and move them across the screen

    """

    def __init__(self):
        self.cars = []  # list of Turtle objects
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        """
        move each car on the screen
        """
        for car in self.cars:
            car.backward(self.speed)

    def generate_car(self):
        """
        generate one car with random position on the screen.
        :return:
        """
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color("black", random.choice(COLORS))
        new_car.penup()
        rand_y = random.randint(-250, 250)
        new_car.setposition(300, rand_y)
        self.cars.append(new_car)

    def increase_speed(self):
        """
        increase the speed attribute by 10
        """
        self.speed += MOVE_INCREMENT
