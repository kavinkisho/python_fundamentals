import turtle
import random

# Settings
turtle.shape("classic")
turtle.speed("normal")
turtle.Screen().colormode(255)
turtle.Screen().bgcolor("#96a2f2")
radius = 50
x_loc = -420
y_loc = 290




def DrawAndFillCircle():
    # Pick a random colour
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.color(r, g, b)

    # draw and fill circle
    turtle.begin_fill()
    turtle.circle(radius, 360)
    turtle.end_fill()


#numCircles = int(input("Enter number of circles: "))

# Move to start position
turtle.penup()
turtle.goto(x_loc, y_loc)
turtle.pendown()


for j in range(5):

    # Draw 1 Row
    for i in range(5):
        DrawAndFillCircle()
        x_loc = x_loc + (radius * 2)
        turtle.penup()
        turtle.goto(x_loc, y_loc)
        turtle.pendown()

    # Move to the next row
    y_loc = y_loc - (radius * 2)
    x_loc = -420
    turtle.penup()
    turtle.goto(x_loc, y_loc)
    turtle.pendown()



turtle.mainloop()











