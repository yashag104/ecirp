from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_count = 0
        self.r_count = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 300)
        self.write(f"{self.l_count} :SCORE: {self.r_count}", align="center", font=("Courier", 20, "normal"))

    def l_score(self):
        self.l_count += 1
        self.update()

    def r_score(self):
        self.r_count += 1
        self.update()

    def over(self, winner):
        self.clear()
        self.goto(0, 100)
        self.write(arg=f"{self.l_count} :FINAL SCORE: {self.r_count}", align="center", font=("Courier", 40, "normal"))
        self.goto(0, 0)
        self.write(arg=f"{winner} paddle wins the game.", align="center", font=("Courier", 40, "normal"))
