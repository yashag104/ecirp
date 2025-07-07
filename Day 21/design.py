from turtle import Turtle


class Design(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-390, 300)
        self.pendown()
        self.draw_boundary()
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(50, 0)
        self.pendown()
        self.circle(50, None, 360)

    def draw_boundary(self):
        for _ in range(2):
            self.forward(780)
            self.right(90)
            self.forward(600)
            self.right(90)
