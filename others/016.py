# Print list in reverse order using a loop
# Given:

# list1 = [10, 20, 30, 40, 50]
# Expected output:

# 50
# 40
# 30
# 20
# 10
def display_reversed_list(l: list):
    for i in range(len(l)-1, -1, -1):
        print(l[i])

if __name__ == "__main__":
    display_reversed_list([10, 20, 30, 40, 50])
    display_reversed_list([15, 24, 32, 13, 67])
