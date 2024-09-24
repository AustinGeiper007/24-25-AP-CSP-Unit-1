total = 0
increment = int(input("Enter a increment to increase by: "))
Goal = int(input("Enter a goal to increase to: "))
while total + increment <= 852:
    total += increment

print("Your total is: " + str(total))
print("Which is as high as you can go")
print("counting by 11, without exceeding 852")