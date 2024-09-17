import turtle as trtl

painter = trtl.Turtle()


x = 0
y = 0
z = 0
painter.turtlesize(5)
for num in range(200):
    painter.pencolor(x, y, z)
    painter.forward(1)







wn = trtl.Screen()
wn.mainloop()