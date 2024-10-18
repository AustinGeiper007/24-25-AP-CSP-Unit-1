import turtle as trtl
import random as rd

# sky code here (makes background with just a really big circle)
# Finished
sky = trtl.Turtle()
sky.speed(0)
sky.color('#00a6ff')
sky.pensize(5000)
sky.circle(100)
sky.hideturtle()

# sun code
# Finished
sun = trtl.Turtle()
sun.hideturtle()
sun.speed(0)
sun.pensize(75)
sun.color('yellow')
# Set up sun
sun.penup()
sun.goto(-400, 300)
sun.pendown()
sun.showturtle()
sun.circle(5)
# Rays
sun.pensize(5)
for ray in range(8):
    sun.hideturtle()
    sun.penup()
    sun.goto(-400, 305)
    sun.setheading((ray * 45) + 10)
    sun.forward(60)
    sun.pendown()
    sun.showturtle()
    sun.forward(30)
sun.hideturtle()

# ground code
#Finished
grass = trtl.Turtle()
grass.hideturtle()
grass.speed(0)
grass.color('#3f9b0b')
grass.pensize(250)
grass.penup()
grass.goto(-500, -350)
grass.pendown()
grass.showturtle()
grass.forward(1000)
grass.hideturtle()

#cloud code
cloud = trtl.Turtle()
cloud.color('white')
cloud.pensize(50)
cloud.penup()
cloud.goto(400, 300)
cloud.pendown()
cloud.circle(5)
cloud.penup()
cloud.goto(360, 310)
cloud.pendown()
cloud.circle(5)

# house code
house = trtl.Turtle()





# the loop stuff to keep it there
wn = trtl.Screen()
wn.mainloop()