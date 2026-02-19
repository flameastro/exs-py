# ex293: Create a function that print out the array in reverse order using a for loop.
# Given:

# array = [10, 20, 30, 40, 50]
# Expected output: [50, 40, 30, 20, 10]
def inverse(array):
    inverted_array = []

    for x in range(len(array)-1, -1, -1):
        inverted_array.append(array[x])

    return inverted_array


if __name__ == "__main__":
    print(inverse([1, 2, 3]))
    print(inverse([10, 5, 0]))
    print(inverse([5, 6, 7, 1, 2]))
