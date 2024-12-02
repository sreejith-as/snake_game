from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class ScoreBoard(Turtle):
    """A class to manage the scoring system using the Turtle graphics library."""

    def __init__(self):
        """Initializes the ScoreBoard object, sets the initial score, 
        retrieves the high score from a file, and updates the scoreboard display."""
        super().__init__()
        self.color("White")  # Set the color of the text to white
        self.penup()  # Prevent the turtle from drawing lines
        self.goto(x=0, y=270)  # Position the scoreboard at the top center of the screen
        self.score = 0  # Initialize the current score to 0
        with open("data.txt") as data:
            self.high_score = int(data.read())  # Read the high score from a file
        self.hideturtle()  # Hide the turtle cursor
        self.update_scoreboard()  # Update the scoreboard display

    def update_scoreboard(self):
        """Clears the previous scoreboard display and writes the current score and high score."""
        self.clear()  # Clear the previous text
        # Write the current score and high score at the center of the screen
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the current score to 0. If the current score is greater than the high score,
        updates the high score and saves it to a file."""
        if self.score > self.high_score:  # Check if the current score is a new high score
            self.high_score = self.score  # Update the high score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # Write the new high score to the file
        self.score = 0  # Reset the current score to 0
        self.update_scoreboard()  # Update the scoreboard display

    def increase_score(self):
        """Increases the current score by 1 and updates the scoreboard display."""
        self.score += 1  # Increment the score
        self.update_scoreboard()  # Update the scoreboard display

    # def game_over(self):
    #     """Displays a 'Game Over' message at the center of the screen."""
    #     self.goto(x=0, y=0)  # Move to the center of the screen
    #     self.write(f"Game Over", align="center", font=FONT)  # Write 'Game Over' message