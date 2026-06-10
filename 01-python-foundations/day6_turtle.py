from turtle import Turtle as t, Screen

timmy = t()
timmy.shape("turtle")
timmy.color("orchid")

joe = t()
joe.shape("turtle")
joe.color("aquamarine")
for index in range(0,4):
    timmy.forward(100)
    timmy.right(90)

joe.teleport(-500,200)
x=-500
for line_index in range(0, 15):
    joe.forward(10)
    joe.penup()
    x += 20
    joe.goto(x, 0)
    joe.pendown()
    joe.forward(10)
    joe.penup()

screen = Screen()
screen.exitonclick()
