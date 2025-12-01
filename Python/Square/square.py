# importing the library
import turtle

# creating canvas
turtle.Screen().bgcolor("red")

sc = turtle.Screen()
sc.setup(800, 600)

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
    board.forward(100)
    board.left(90)

# repeat

# keep window open
turtle.done()
