# ex200: Given an array of integers, return a new array with each value doubled. For example:
# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    return list(map(lambda i: i * 2, a))


if __name__ == "__main__":
    print(maps([1, 2, 3]))  # [2, 4, 6]
    print(maps([8, 16, 24]))  # [16, 32, 48]
    print(maps([128, 256, 512]))  # [256, 512, 1024]
