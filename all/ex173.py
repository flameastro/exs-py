# ex173: Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed. For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7. [10, 343445353, 3453445, 3453545353453] should return 3453455.
def sum_two_smallest_numbers(numbers: list):
    return sum(sorted(numbers)[:2])

    # numbers.sort()
    # lowest_numbers = [numbers[0], numbers[1]]

    # return sum(lowest_numbers)


if __name__ == "__main__":
    print(sum_two_smallest_numbers([8, 3, 2, 9]))  # 5
    print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # 7
    print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))  # 3453455
    print(sum_two_smallest_numbers([0, 12, 3, 7]))  # 3
