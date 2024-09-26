''' How to multiply 6*5 (repeated addition)
num = 0
product = 0
for num in range(5):
    product += 6
print(product)
'''

# This shows the stages of math with nested loops
# Counting, Adding, Multiplication
# More layers would show exponentiation, tritration, tetration, and so on
num1 = 0
num2 = 0
total = 0
for num1 in range(50):
    for num2 in range(5):
        total += 1

print(total)