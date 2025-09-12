# ex192: Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]
def reverse_seq(n):
    return [x for x in range(n, 0, -1)]


if __name__ == "__main__":
    print(reverse_seq(12))  # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(reverse_seq(25))  # [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(reverse_seq(2))  # [2, 1]
    print(reverse_seq(-1))  # []
