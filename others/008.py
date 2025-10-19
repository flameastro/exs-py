# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:

# result list: [25, 35, 40, 60, 90]
def add_even_odd(list1: list, list2: list):
    l = [x for x in list1 if x % 2 == 1]
    l += [y for y in list2 if y % 2 == 0]

    return l

if __name__ == "__main__":
    print(add_even_odd([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))  # [25, 35, 40, 60, 90]
    print(add_even_odd([12, 45, 65, 25, 34, 20], [64, 63, 25, 78, 90, 3, 77]))  # [45, 65, 25, 64, 78, 90]
