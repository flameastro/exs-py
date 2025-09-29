# ex254: Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

# Examples
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
def powers_of_two(n):
    return [2 ** i for i in range(0, n+1)]


if __name__ == "__main__":
    print(powers_of_two(0))  # [1]
    print(powers_of_two(1))  # [1, 2]
    print(powers_of_two(2))  # [1, 2, 4]
    print(powers_of_two(3))  # [1, 2, 4, 8]
    print(powers_of_two(4))  # [1, 2, 4, 8, 16]
    print(powers_of_two(5))  # [1, 2, 4, 8, 16, 32]
    print(powers_of_two(35))  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368]
