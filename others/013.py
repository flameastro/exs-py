# Calculate sum of all numbers from 1 to a given number
# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# Expected Output:

# Enter number 10
# Sum is:  55
number = int(input("Give the number: "))
s = 0

for n in range(1, number+1):
    s += n

print(f"The Sum IS: {s}")
