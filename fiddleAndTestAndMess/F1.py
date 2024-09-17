import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)

step = 1

while True:
    painter.forward(step)
    step = step + 1
    painter.left(90)






wn = trtl.Screen()
wn.mainloop()