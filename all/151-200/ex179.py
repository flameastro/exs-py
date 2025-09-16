# ex179: Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b. Note: a and b are not ordered!
def get_sum(a, b):
    return sum([i for i in range(a, b+1)] if a < b else [i for i in range(b, a+1)])


if __name__ == "__main__":
    print(get_sum(1, 0))
    print(get_sum(1, 2))
    print(get_sum(0, 1))
    print(get_sum(1, 1))
    print(get_sum(-1, 0))
    print(get_sum(-1, 2))
