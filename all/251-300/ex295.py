# ex295: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
# Given:
# str1 = "James"
# Expected Output:
# Jms
def first_middle_last(string):
    if len(string) < 3:
        return "The string need to have more than 3 letters."

    return f"{string[0]}{string[len(string) // 2]}{string[-1]}"


if __name__ == "__main__":
    print(first_middle_last("James"))  # Jms
    print(first_middle_last("MIT"))  # boi
    print(first_middle_last("Harvard University"))  # Hny


