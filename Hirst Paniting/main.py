import turtle
import random
tim = turtle.Turtle()
turtle.colormode(255)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(10):
    for n in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)
screen = turtle.Screen()
screen.exitonclick()
