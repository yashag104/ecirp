from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
import time
from ball import Ball
from design import Design
DECREMENT = 1

screen = Screen()
screen.setup(800, 680)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()
ball = Ball()
design = Design()


screen.listen()
screen.onkeypress(r_paddle.go_up,  "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up,  "w")
screen.onkeypress(l_paddle.go_down, "s")

game = True
while game:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    l_score = 0
    r_score = 0
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
        ball.move_speed *= DECREMENT
    if l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= DECREMENT
    if r_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.xcor() > 360:
        score.l_score()
        ball.goto(0, 0)
        ball.bounce_x()
    if ball.xcor() < -360:
        score.r_score()
        ball.goto(0, 0)
        ball.bounce_x()
    if score.l_count == 10 or score.r_count == 1:
        if score.l_count == 10:
            score.over("Left")
        else:
            score.over("Right")
        game = False
    score.update()


screen.exitonclick()
