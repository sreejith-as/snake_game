import random
from turtle import Turtle

class Food(Turtle):
    """A class to represent food for a turtle graphics game.

    Inherits from the Turtle class and represents a piece of food that
    can be displayed on the screen. The food is represented as a blue
    circle that can be repositioned randomly within specified bounds.
    """

    def __init__(self):
        """Initialize the Food object.

        This method sets the shape, color, size, and initial position of
        the food. The food is placed at a random position within the
        coordinates (-280, 280) for both x and y axes.
        """
        super().__init__()  # Initialize the parent Turtle class
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Prevent drawing lines when the turtle moves
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the turtle's speed to the fastest
        # Generate random x and y coordinates for the food's position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # Move the food to the random position

    def refresh(self):
        """Reposition the food to a new random location.

        This method generates new random x and y coordinates and moves
        the food to this new position, effectively refreshing its location
        on the screen.
        """
        random_x = random.randint(-280, 280)  # Generate new random x coordinate
        random_y = random.randint(-280, 280)  # Generate new random y coordinate
        self.goto(random_x, random_y)  # Move the food to the new random position