import turtle as trtl
spider = trtl.Turtle()

#body
spider.pensize(70)
spider.color("black")
spider.penup()
spider.goto(0, 55)
spider.pendown()
spider.circle(35)

#head
spider.pensize(40)
spider.penup()
spider.goto(0, 0)
spider.pendown()
spider.circle(10)

#legs
spider.pensize(5)


# Spider currently only has 2 legs
# add another loop and some variables to add legss
for num2 in range(2):
    if num2%2 == 0:
        z = 1
    else:
        z = -1
    spider.setheading(15 * z)
    spider.penup()
    spider.goto(0, 55)
    spider.pendown()
    spider.circle(120, 120 * z, 4)
    spider.penup()
    spider.goto(0, 70)
    spider.pendown()
    spider.setheading(15 * z)
    spider.circle(90, 120 * z, 4)







wn = trtl.Screen()
wn.mainloop()