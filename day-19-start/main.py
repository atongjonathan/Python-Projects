from turtle import Turtle, Screen
import random

screen = Screen()

# timmy = Turtle()

#
#
# def move_forwards():
#     timmy.forward(5)
#
#
# def move_backwards():
#     timmy.backward(5)
#
#
# def move_right():
#     new_heading = timmy.heading()+10
#     timmy.setheading(new_heading)
#
#
# def move_left():
#     new_heading = timmy.heading() - 10
#     timmy.setheading(new_heading)
#
#
# def clear():
#     timmy.home()
#     timmy.clear()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="c", fun=clear)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race. Enter a color").lower()

y_position = -100
my_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position)
    y_position += 50
    my_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in my_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = (turtle.pencolor())
            if winning_color == user_bet:
                print(f"You've Won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost. The {winning_color} turtle is the winner!")






screen.exitonclick()
