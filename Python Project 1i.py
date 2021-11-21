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
    pattern.pencolor(colors[i%7])

# child loop 1 to run 4 times    
    for j in range(4):

# child loop 2 to run 2 times
        for k in range(2):

# turtle moves forward by 150 units
            pattern.forward(150)

# turtle turns to the left by 30 degrees
            pattern.left(30)

# turtle moves forward by 150 units
            pattern.forward(150)

# turtle turns to the left by 150 degrees
            pattern.left(150)

# turtle turns to the left by 10 degrees
    pattern.left(10)

# stop the code execution
pattern.done()
