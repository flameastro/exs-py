# ex257: You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.
def two_sort(array):
    return "***".join(list(sorted(array)[0]))


if __name__ == "__main__":
    print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))  # b***i***t***c***o***i***n
    print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))  # a***r***e
    print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]))  # c***o***d***e
