import colorgram

import random
import turtle
from turtle import Turtle, Screen


colors = colorgram.extract('pic.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    new_color = (r, g, b)
    rgb_colors.append(new_color)
colors_list = [
    (0, 0, 0),  # Black
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 192, 203),  # Pink
    (128, 0, 128),  # Purple
    (255, 165, 0),  # Orange
    (0, 128, 0),  # Dark Green
    (128, 0, 0),  # Maroon
    (128, 128, 128),  # Gray
    (255, 215, 0),  # Gold
    (192, 192, 192),  # Silver
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (165, 42, 42),  # Brown
    (173, 216, 230),  # Light Blue
    (255, 105, 180),  # Hot Pink
    (148, 0, 211)  # Dark Violet
]


# print(rgb_colors)
timmy = Turtle()
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.setpos(-250, -200)
current_position = -150
for _ in range(10):
    for _ in range(10):
        color = random.choice(colors_list)
        timmy.dot(20, color)
        timmy.forward(50)
    timmy.setpos(-250, current_position)
    current_position += 50

screen = Screen()
screen.exitonclick()
