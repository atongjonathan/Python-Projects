from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level:{self.score}", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
