from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def start_again(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def move_left(self):
        self.goto(self.xcor() - 20, self.ycor())
        self.setheading(90)

    def move_right(self):
        self.goto(self.xcor() + 20, self.ycor())
        self.setheading(90)
