# to import package
import turtle as pattern

# to view in full screen
screen = pattern.Screen()

# to set the screen size
screen.setup(width = 1.0, height = 1.0)

# to remove close, minimize, maximize buttons
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

# turtle window background color
pattern.bgcolor("black")

# turtle pen width
pattern.pensize(3)

# turtle speed
pattern.speed(0)

# to hide the turtle
pattern.hideturtle()

# create a variable, dataType = list
colors = ["#0000FF", "#00FF00"]

# moves the turtle up
pattern.penup()

# turtle moves -200 on x axis & -100 on y axis
pattern.goto(-200,-100)

# moves the turtle down
pattern.pendown()

# parent loop to run 60 times
for i in range(60):

# child loop to run 2 times
   for j in colors:

# color of the turtle, where j represents the color
      pattern.color(j)

# turtle moves forward by 400 units
      pattern.forward(400)

# turtle turns to the left by 121 degrees
      pattern.left(121)

# stop the code execution
pattern.done()