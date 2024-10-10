#   a118_grades.py
#   This code is incomplete.
from telnetlib import STATUS

my_courses = ["English", "Math", "CS"]
my_grades = []

def letter_grade_calc():
    if class_grade <= 100 and class_grade >= 90:
        print("You got an A in: " + c)
    elif class_grade < 89 and class_grade >= 80:
        print("You got an B in: " + c)
    elif class_grade < 79 and class_grade >= 70:
        print("You got an C in: " + c)
    elif class_grade < 69 and class_grade >= 65:
        print("You got an D in: " + c)
    elif class_grade < 64 and class_grade >= 0:
        print("You failed in: " + c)
    elif class_grade < 0:
        print("How? How did you get a negative grade? That's not supposed to be possible")
    else:
        print("Invalid Input")


for c in my_courses:
    while STATUS:
        class_grade = int(input("Enter your grade in " + c + ":"))
        my_grades.append(class_grade)
        letter_grade_calc()