from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Set up the screen for the Snake game
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the window
screen.bgcolor("black")               # Set the background color of the window
screen.title("Snake Game")             # Set the title of the window
screen.tracer(0)                       # Turn off the screen updates for smoother animation

# Initialize game components
snake = Snake()                         # Create a new Snake object
food = Food()                           # Create a new Food object
scoreboard = ScoreBoard()               # Create a new ScoreBoard object

# Listen for key presses to control the snake
screen.listen()
screen.onkey(snake.up, "Up")           # Move the snake up when the Up arrow key is pressed
screen.onkey(snake.down, "Down")       # Move the snake down when the Down arrow key is pressed
screen.onkey(snake.left, "Left")       # Move the snake left when the Left arrow key is pressed
screen.onkey(snake.right, "Right")     # Move the snake right when the Right arrow key is pressed

# Main game loop
game_is_on = True                       # Flag to control the game loop

while game_is_on:
    screen.update()                    # Update the screen to show the latest game state
    time.sleep(0.1)                   # Pause the loop for a short duration to control the game speed
    snake.move()                       # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15: # Check if the snake's head is close enough to the food
        food.refresh()                 # Refresh the food's position
        snake.extend()                 # Extend the snake's length
        scoreboard.increase_score()    # Increase the score on the scoreboard

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()             # Reset the scoreboard if the snake collides with the wall
        snake.reset()                  # Reset the snake's position and length

    # Detect collision with tail
    for segment in snake.segments[1:]: # Loop through the snake's segments (excluding the head)
        if snake.head.distance(segment) < 10: # Check if the snake's head is close to any of the segments
            scoreboard.reset()         # Reset the scoreboard if the snake collides with its own tail
            snake.reset()              # Reset the snake's position and length

# Close the game window when clicked
screen.exitonclick()
