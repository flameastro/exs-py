# ex203: Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).
# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


if __name__ == "__main__":
    print(odd_or_even([12, 3, 2, 2, 2, 2, 1]))  # even
    print(odd_or_even([21, 8]))  # odd
    print(odd_or_even([0]))  # even
