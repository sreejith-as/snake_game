from turtle import Turtle

# Constants for the initial positions of the snake segments, movement distance, and heading directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """A class representing a snake in a turtle graphics environment."""
    
    def __init__(self):
        """Initialize the Snake object by creating its segments and setting the head."""
        self.segments = []  # List to hold the segments of the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Set the head of the snake to the first segment

    def create_snake(self):
        """Create the initial snake with segments at the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add each segment at the predefined starting positions

    def add_segment(self, position):
        """Add a new segment to the snake at the given position.

        Args:
            position (tuple): The (x, y) coordinates where the new segment should be placed.
        """
        new_segment = Turtle(shape="square")  # Create a new turtle segment with a square shape
        new_segment.color("white")  # Set the color of the segment to white
        new_segment.penup()  # Prevent the segment from drawing lines
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the new segment to the list of segments

    def reset(self):
        """Reset the snake to its initial state by moving segments off-screen and recreating the snake."""
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move each segment off-screen
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Create a new snake
        self.head = self.segments[0]  # Reset the head to the new first segment

    def extend(self):
        """Add a new segment to the snake by extending it at the position of the last segment."""
        self.add_segment(position=self.segments[-1].position())  # Add a segment at the last segment's position

    def move(self):
        """Move the snake forward by updating the position of each segment."""
        for seg_number in range(len(self.segments) - 1, 0, -1):
            # Move each segment to the position of the segment in front of it
            new_x = self.segments[seg_number - 1].xcor()  # Get the x-coordinate of the segment in front
            new_y = self.segments[seg_number - 1].ycor()  # Get the y-coordinate of the segment in front
            self.segments[seg_number].goto(new_x, new_y)  # Move the current segment to the new position
        self.segments[0].forward(MOVE_DISTANCE)  # Move the head forward by the defined move distance

    def up(self):
        """Change the direction of the snake's head to up if it is not currently moving down."""
        if self.head.heading() != DOWN:  # Check that the snake is not moving down
            self.head.setheading(UP)  # Set the heading of the head to up

    def down(self):
        """Change the direction of the snake's head to down if it is not currently moving up."""
        if self.head.heading() != UP:  # Check that the snake is not moving up
            self.head.setheading(DOWN)  # Set the heading of the head to down

    def left(self):
        """Change the direction of the snake's head to left if it is not currently moving right."""
        if self.head.heading() != RIGHT:  # Check that the snake is not moving right
            self.head.setheading(LEFT)  # Set the heading of the head to left

    def right(self):
        """Change the direction of the snake's head to right if it is not currently moving left."""
        if self.head.heading() != LEFT:  # Check that the snake is not moving left
            self.head.setheading(RIGHT)  # Set the heading of the head to right