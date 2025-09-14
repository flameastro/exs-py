# ex206: Given an array of integers, return the element that appears only once in the array.
def unic(arr):
    return [n for n in arr if arr.count(n) == 1][-1]


if __name__ == "__main__":
    print(unic([15, 15, 15, 12]))  # 12
    print(unic([3, 3, 3, 2, 3, 3]))  # 2
    print(unic([25, 12, 12, 12, 12, 12]))  # 25
