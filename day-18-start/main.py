from turtle import Turtle, Screen
import random
import turtle
side = [0, 90, 180, 270]
timmy = Turtle()
# timmy.shape("arrow")
timmy.color("red")
timmy.speed("fastest")


# number_of_sides = 3
# while number_of_sides < 9:
#     for _ in range(number_of_sides):
#         timmy.forward(100)
#         timmy.right(360/number_of_sides)
#     number_of_sides += 1
#     timmy.color(random.choice(colors))
# timmy.pensize(10)

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_colors = (r, g, b)
    return my_colors


#
#
# for _ in range(200):
#     timmy.setheading(random.choice(side))
#     timmy.forward(30)
def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)
        timmy.circle(100)
        timmy.color(random_color())


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
