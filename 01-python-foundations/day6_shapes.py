from turtle import Turtle, Screen
import random

class Shape:
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color

    # We pass the active turtle instance ('drawer') as an explicit dependency
    def draw(self, drawer):
        drawer.color(self.color)
        angle = 360 / self.sides
        for _ in range(self.sides):
            drawer.forward(100)
            drawer.right(angle)

screen = Screen()

# 1. Provision a SINGLE execution engine instance
tony = Turtle()

# 2. Pipeline Configuration: Streamlining your repeated assignments into a list container
shape_configs = [
    (3, "IndianRed1"),
    (4, "darkseagreen"),
    (5, "cyan4"),
    (6, "burlywood"),
    (7, "firebrick"),
    (8, "khaki"),
    (9, "lightsalmon"),
    (10, "gold")
]

# 3. High-Velocity Loop Execution
for sides, color in shape_configs:
    active_shape = Shape(sides, color)
    active_shape.draw(tony) # Injecting the single turtle 'tony' to do all the work

screen.exitonclick()