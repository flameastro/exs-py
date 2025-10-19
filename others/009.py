# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# Given:

# number = 7536
# # Output 6 3 5 7
number = str(int(input("Type an integer number: ")))

print(" ".join(reversed(list(number))))
