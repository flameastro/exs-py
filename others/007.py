# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number
number = str(int(input("Type an integer: ")))
inverted_number = number[::-1]
if inverted_number == number:
    print(f"Yes. given number is palindrome number ({number} == {inverted_number})")
else:
    print(f"No. given number is not palindrome number ({number} != {inverted_number})")
