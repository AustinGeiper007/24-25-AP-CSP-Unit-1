
status = True

def redo():
    ans = input("Would you like to do another operation? (y/n)")
    if ans == 'y':
        print("Enter new number")
    elif ans == 'n':
        print("Thank You. Good Bye")
        status = False
    else:
        print("Please enter y or n")

while status:
    num = int(input("Enter a number -> "))
    if (num < 60):
        print("You failed...")
        redo()
    elif (num >= 64 and num < 70):
        print("You got a D")
        redo()
    elif (num >= 70 and num < 80):
        print("You got a C")
        redo()
    elif (num >= 80 and num < 90):
        print("You got a B")
        redo()
    elif (num >= 90 and num < 101):
        print("You got an A. YIPPEE")
        redo()
    else:
        print("INVALID INPUT. PLEASE TRY AGAIN")
