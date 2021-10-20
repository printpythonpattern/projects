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

# turtle speed 
pattern.speed(0)

# turtle window title
pattern.title('Spiral Hexagon')

# to hide the turtle
pattern.hideturtle() 

# create a variable, dataType = list
colors = ["#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]

# parent loop to run 300 times
for i in range(300):

# turtle pen color
    pattern.pencolor(colors[i%6])

# turtle pen width
    pattern.pensize(i/80 + 1)

# turtle moves forward by i units
    pattern.forward(i)

# turtle turns to the left by 59 degrees
    pattern.left(59)

# stop the code execution
pattern.done()
