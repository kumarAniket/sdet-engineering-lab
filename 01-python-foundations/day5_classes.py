# OOP Concepts

from turtle import Turtle, Screen

# Object Attributes
bubbles = Turtle()
print(bubbles)
bubbles.shape('turtle')
bubbles.color('coral')

bubbles.forward(100)
bubbles.right(90)
bubbles.forward(100)
bubbles.right(90)
bubbles.forward(100)
bubbles.right(90)
bubbles.forward(105)

my_screen = Screen()
print(my_screen.canvheight)

# Object Methods - Functions tied to an object

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Pokemon Name', 'Type']
table.add_row(['Pikachu','Electric'])
table.add_divider()
table.add_row(['Squirtle','Water'])
table.add_divider()
table.add_row(['Charmander','Fire'])

table.align='l'

print(table)