#   a114_divisible.py
# get two numbers from user
num = int(input("Enter Numerator (number 1): "))
dem = int(input("Enter Denominator (number 2): "))
# loop while the numbers are not divisible (the remainder is not 0)
while (num%dem) != 0:
    # inform user of result
    print("These 2 numbers are not divisible")
    # gather user input again
    num = int(input("Enter Numerator (number 1): "))
    dem = int(input("Enter Denominator (number 2): "))
# inform user of result
print("These 2 numbers are divisible!")