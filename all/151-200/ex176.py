# ex176: # Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest. Write a function that returns both the minimum and maximum number of the given list/array.
# Examples (Input --> Output)
# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]
def min_max(numbers: list):
    return [sorted(numbers)[i] for i in range(0, -2, -1)]


if __name__ == "__main__":
    print(min_max([8, 4, 2, 6, 1, 2, 8]))  # [1, 8]
    print(min_max([0, 5]))  # [0, 5]
    print(min_max([23, 12, 5, -8, 2]))  # [-8, 23]
