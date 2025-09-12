# ex187: Implement a function which convert the given boolean value into its string representation. Note: Only valid inputs will be given.
def boolean_to_string(b):
    return "True" if b else "False"


if __name__ == "__main__":
    print(boolean_to_string(True))  # "True"
    print(boolean_to_string(False))  # "False"
