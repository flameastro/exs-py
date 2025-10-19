# Write a Python code to remove characters from a string from 0 to n and return a new string.

# Given:

# def remove_chars(word, n):
#     # write your code

# print("Removing characters from a string")
# print(remove_chars("pynative", 4)) 
# # output 'tive' first four characters are removed

# print(remove_chars("pynative", 2)) 
# # output 'native'
def remove_chars(word, n):
    if n >= len(word):
        return "The value of n need to be lower than the length of the word."

    return word[n:]


if __name__ == "__main__":
    print(remove_chars("pynative", 4))  # tive
    print(remove_chars("pynative", 2))  # native
    print(remove_chars("pythonpython", 16))  # The value of n need to be lower than the length of the word.
    print(remove_chars("pythonpython", 11))  # n
