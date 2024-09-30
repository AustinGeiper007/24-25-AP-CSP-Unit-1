#   a116_buggy_image.py
#   1.1.6 Step 5 After fixing
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()

painter.pensize(40)
painter.circle(20)

legCount = 6
length = 70
legAngle = 380 / legCount

painter.pensize(5)

num = 0

while (num < legCount):
  painter.goto(0, 0)
  painter.setheading(legAngle * num)
  painter.forward(length)
  num = num + 1

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()