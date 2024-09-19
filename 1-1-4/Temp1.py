num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    print(f"{num1} > {num2}")
elif num2 > num1:
    print(f"{num2} > {num1}")
elif num1 == num2:
    print("Numbers are the same")