import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)

step = 1
turn = 1

while True:
    painter.forward(step)
    step = step + 1
    painter.left(turn)
    turn = turn + 1
    if step == 250:
        step = 1
        turn = 1



wn = trtl.Screen()
wn.mainloop()