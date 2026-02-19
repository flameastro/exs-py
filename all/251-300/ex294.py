# ex294: Create a function to print elements from a given list present at odd index positions
# Given:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output: [20, 40, 60, 80, 100]

def odd_positions(array):
    odd_array = []

    for x in range(len(array)):
        if x % 2 != 0:
            odd_array.append(array[x])

    return odd_array


if __name__ == "__main__":
    print(odd_positions([1, 2, 3, 4, 5]))  # [2, 4]
    print(odd_positions([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # [20, 40, 60, 80, 100]
    print(odd_positions([25, 12, 34, 5]))  # [12, 5]
