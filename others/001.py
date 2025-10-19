# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# Given 1:

# number1 = 20
# number2 = 30
# Expected Output:

# The result is 600
# Given 2:

# number1 = 40
# number2 = 30
# Expected Output:

# The result is 70
number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))

product = number1 * number2

if product <= 1000:
    print(f"The result is {product}")
