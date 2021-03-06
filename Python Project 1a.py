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
pattern.title('Rainbow Spirograph')

# to hide the turtle
pattern.hideturtle() 

# create a variable, dataType = list
colors = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]

# parent loop to run 6 times
for i in range(6):

# child loop to run 7 times
   for j in colors:

# creating a condition
      if i == 5 and j == "#4B0082":

# when the condition is true, exit the child loop
         break

# color of the circle, where j represents the color
      pattern.color(j)

# draw a circle of radius 150 units
      pattern.circle(150)

# turtle turns to the left by 10 degrees
      pattern.left(10)

# stop the code execution
pattern.done()
