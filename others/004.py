# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# # output True

# numbers_y = [75, 65, 35, 75, 30]
# # Output False
def same_numbers(l: list):
    if len(l) <= 1:
        return "The length of the list must be higher than 1."

    return l[0] == l[-1]

print(same_numbers([10, 20, 30, 40, 10]))  # True
print(same_numbers([75, 65, 35, 75, 30]))  # False
print(same_numbers([75]))  # The length of the list must be higher than 1.
