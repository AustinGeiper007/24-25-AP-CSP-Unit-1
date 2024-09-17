import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)

step = 1
turn = 1

for num in range(0,400):
    painter.forward(step)
    step = step + 1
    painter.left(turn)
    turn = turn + 1
    if step == 100:
        step = 1
        turn = 1



wn = trtl.Screen()
wn.mainloop()