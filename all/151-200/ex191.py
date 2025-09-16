# ex191: Given an array of integers. Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative. If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    return [] if not arr else [len(list(filter(lambda x: x > 0, arr))), sum(list(filter(lambda x: x < 0, arr)))]

if __name__ == "__main__":
    print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  # [10, -65]
    print(count_positives_sum_negatives([0, 1]))  # [1, 0]
    print(count_positives_sum_negatives([23, -9, -1, 2]))  # [2, -10]
    print(count_positives_sum_negatives([15, 23, 34, 34, 34, 15]))  # [6, 0]