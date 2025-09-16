# ex194: Description: We need a function that can transform a string into a number. What ways of achieving this do you know? Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7
def string_to_number(s):
    return int(s)

if __name__ == "__main__":
    print(string_to_number("28931"))  # 28931
    print(string_to_number("34552"))  # 34552
    print(string_to_number("4"))  # 3
    print(string_to_number("42343124"))  # 42343124
