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
colors = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]

# parent loop to run 36 times
for i in range(36):

# turtle pen color
        pattern.pencolor(colors[i % 7])

# turtle moves forward by 100 units
        pattern.forward(100)

# turtle turns to the right by 30 degrees
        pattern.right(30)

# turtle moves forward by 100 units
        pattern.forward(100)

# turtle turns to the right by 30 degrees
        pattern.right(30)

# turtle moves forward by 100 units
        pattern.forward(100)

# turtle moves 0 on x axis & 0 on y axis
        pattern.goto(0, 0)

# turtle turns to the right by 10 degrees
        pattern.right(10)

# stop the code execution
pattern.done()