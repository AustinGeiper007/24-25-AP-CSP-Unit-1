import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)

# Virus Ball thing? IDEK I messed around and found out
step = 1
turn = 1

for step in range(0, 180):
    painter.forward(step)
    step = step + 1
    painter.left(turn)
    turn = turn + 1
    if step == 185:
        step = 1
        turn = 1



wn = trtl.Screen()
wn.mainloop()