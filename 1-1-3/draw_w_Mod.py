import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# number of towers
num_tower = int(input("How many towers would you like to make?"))

# height of tower and a counter for each floor
num_floors = int(input("How many floors would you like?"))

# iterate
for towers in range(num_tower):
    for floor in range(num_floors):
        # set placement and color of turtle
        painter.penup()
        painter.goto(x, y)
        if floor % 3 == 2:
            painter.color("red")
        else:
            painter.color("blue")
        y = y + 5  # location of next floor

        # draw the floor
        painter.pendown()
        painter.forward(50)
    y = -150
    x = x + 75
    painter.penup()
    painter.goto(x, y)

wn = trtl.Screen()
wn.mainloop()