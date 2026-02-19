# ex297: Removal all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'

# Expected Output: 2510
def just_integers(string):
    integers = ""

    for x in string:
        if x in "0123456789":
            integers = integers + x

    return integers


if __name__ == "__main__":
    print(just_integers("I am 25 years and 10 months old"))  # 2510
    print(just_integers("My name is Mario"))  # 
    print(just_integers("With 21 years, Albert Einstein domains more than 90% of the physics"))  # 2190
