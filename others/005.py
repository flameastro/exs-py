# Write a Python code to display numbers from a list divisible by 5

# Expected Output:

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55
def divisible_numbers(l: list):
    for x in l:
        if x % 5 == 0:
            yield x


if __name__ == "__main__":
    for n in divisible_numbers([10, 20, 33, 46, 55]):
        print(n)  # 10;      20;      55

    for n in divisible_numbers([14, 50, 65, 12, 34]):
        print(n)  # 50;     65
