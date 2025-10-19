# Display numbers from a list using a loop
# Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected output:

# 75
# 150
# 145
def display_right_numbers(l: list):
    for x in l:
        if x > 500:
            break

        if x % 5 == 0 and x <= 150:
            print(x)


if __name__ == "__main__":
    display_right_numbers([12, 75, 150, 180, 145, 525, 50])
    display_right_numbers([25, 65, 77, 15, 43, 44, 95, 98])
