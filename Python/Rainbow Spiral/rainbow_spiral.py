import turtle 

# create turtle and screen
t = turtle.Turtle()
s = turtle.Screen()

# set background color
s.bgcolor("black")

# set turtle speed and hide it 
t.speed("fastest")
t.hideturtle()

# list of colors to use
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# draw a colorful spiral
for x in range (200): # runs 200 times
    t.pencolor(colors[x % len(colors)])
    t.width(2)
    t.forward(x * 2)
    t.left(59)

# keep window opened
turtle.done()
