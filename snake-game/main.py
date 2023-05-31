from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# TODO: Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.update()
# TODO: Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()

# TODO: Detecting collision with WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # TODO: Detecting collision with TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()
screen.exitonclick()
