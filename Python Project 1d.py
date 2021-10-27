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

# turtle window title
pattern.title('Rainbow Virus')

# to hide the turtle
pattern.hideturtle()

# turtle turns to the right by 90 degrees
pattern.right(90)

# turtle moves to -200 on x axis and 0 on y axis
pattern.goto(-200,0)

# create a variable, dataType = list
colors = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]

# parent loop to run 180 times
for i in range(180):

# turtle pen color
        pattern.pencolor(colors[i % 7])

# turtle turns to the left by 'i' degrees
        pattern.left(i)

# turtle moves forward by i times 3.5 units
        pattern.forward(i*3.5)

# stop the code execution
pattern.done()