# ex197: Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]
def digitize(n):
    return list(reversed([int(s) for s in str(n)]))


if __name__ == "__main__":
    print(digitize(35231))  # [1, 3, 2, 5, 3]
    print(digitize(890324))  # [4, 2, 3, 0, 9, 8]
    print(digitize(2198))  # [8, 9, 1, 2]
