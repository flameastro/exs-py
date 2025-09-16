# ex195: We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"
def number_to_string(num):
    return str(num)


if __name__ == "__main__":
    print(number_to_string(123))  # "123"
    print(number_to_string(999))  # "999"
    print(number_to_string(-100))  # "-100"
