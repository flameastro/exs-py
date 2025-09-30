# ex259: In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]
def reverse_list(list1):
    # return list(reversed(list1))
    # return list1[::-1]
    list2 = []

    for e in list1:
        list2.insert(0, e)

    return list2


if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
    print(reverse_list([9, 12, 4, 5, 3]))  # [3, 5, 4, 12, 9]
    print(reverse_list([9, 45, 2, 3, 1]))  # [1, 3, 2, 45, 9]
