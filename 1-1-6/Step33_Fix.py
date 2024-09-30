#   a116_ladybug.py
#   Workspace for Step33 on pltw 1.1.6
import turtle as trtl

# create ladybug head
ladyBugPainter = trtl.Turtle()
ladyBugPainter.pensize(40)
ladyBugPainter.circle(5)

# and body
ladyBugPainter.penup()
ladyBugPainter.goto(0, -55)
ladyBugPainter.color("red")
ladyBugPainter.pendown()
ladyBugPainter.pensize(40)
ladyBugPainter.circle(20)
ladyBugPainter.setheading(270)
ladyBugPainter.color("black")
ladyBugPainter.penup()
ladyBugPainter.goto(0, 5)
ladyBugPainter.pensize(2)
ladyBugPainter.pendown()
ladyBugPainter.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladyBugPainter.pensize(10)

# draw two sets of dots
while (num_dots <= 4 ):
  ladyBugPainter.penup()
  ladyBugPainter.goto(xpos, ypos)
  ladyBugPainter.pendown()
  ladyBugPainter.circle(3)
  ladyBugPainter.penup()
  ladyBugPainter.goto(xpos + 30, ypos + 15)
  ladyBugPainter.pendown()
  ladyBugPainter.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 2

ladyBugPainter.hideturtle()

wn = trtl.Screen()
wn.mainloop()