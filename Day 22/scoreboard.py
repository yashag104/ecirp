from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
