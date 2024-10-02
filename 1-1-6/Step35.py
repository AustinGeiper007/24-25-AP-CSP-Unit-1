#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# Draw legs on the bug (Not in Step33)
ladybug.pensize(4)
ladybug.penup()
ladybug.goto(0, -40)
ladybug.pendown()
ladybug.setheading(45)
for z in range(2):
    for num in range(3):
        ladybug.forward(60)
        ladybug.right(45)
        ladybug.goto(0, -40)
    ladybug.setheading(225)
ladybug.setheading(0)

# and body
ladybug.pensize(40)
ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 4 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 15)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 2


# hide the painter
ladybug.hideturtle()

#keep window open
wn = trtl.Screen()
wn.mainloop()