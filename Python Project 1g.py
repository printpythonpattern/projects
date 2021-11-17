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
pattern.pensize(2)

# turtle speed 
pattern.speed(0)

# to hide the turtle
pattern.hideturtle()

# create a variable, dataType = list
colors = ["#ff0000", "#ff4000", "#ff8000", "#ffbf00", "#ffff00", "#bfff00", "#80ff00", "#40ff00", "#00ff00", "#00ff40", "#00ff80", "#00ffbf", "#00ffff", "#00bfff", "#0080ff", "#0040ff","#0000ff", "#4000ff", "#8000ff", "#bf00ff", "#ff00ff","#ff00bf", "#ff0080", "#ff0040", "#ff0000"]

# parent loop to run 3 times
for i in range(3):

# child loop 1 to run 25 times
	for j in colors:

# color of the rectangle, where j represents the color
		pattern.color(j)

# turtle turns to the left by 5 degrees
		pattern.left(5)

# child loop 2 to run 4 times
		for s in range(4):

# turtle moves forward by 150 units
			pattern.forward(150)

# turtle turns to the left by 90 degrees
			pattern.left(90)

# turtle moves forward by 75 units
			pattern.forward(75)

# stop the code execution
pattern.done()