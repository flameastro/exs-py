# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

# Expected Output:

# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t
# v
string = input("Type the String: ")
print(f"Original string is {string}")
print("Printing only even index chars")
for l in range(0, len(string)-1, 2):
    print(string[l])


"""
Type the String: PYnative
Original string is PYnative
Printing only even index chars
P
n
t
v
"""