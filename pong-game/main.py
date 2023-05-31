from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() < -340:
        ball.refresh()
        scoreboard.l_point()

    elif ball.xcor() > 340:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()