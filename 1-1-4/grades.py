grade = int(input("Enter grade from last test: "))

if grade == 100
    print("Congratulations! You won!")
elif grade < 100 and grade >= 90:
    print("You got an A on this assessment: Amazing!")
elif grade < 89 and grade >= 80:
    print("You got a B on this assessment: Nice Work!")
elif grade < 79 and grade >= 70:
    print("You got a C on this assessment: Mediocore performance")
elif grade < 69 and grade >= 65:
    print("You got an D on this assessment: You passed, but barely")
elif grade < 64 and grade >= 0:
    print("You got an F on this assessment...You failed")
elif grade < 0:
    print("How? How did you get a negative grade? That's not supposed to be possible")
else:
    print("You got an invalid grade/This isn't a number")