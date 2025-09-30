# ex260: Write a program that takes a string, (1) capitalizes the first letter, (2) creates a list containing each word, and (3) searches for the last occurrence of ”a” in the first word.
string = input("Type the string: ")

print(f"Capitalized: {string.capitalize()}")
print(f"Words: {string.split()}")
print(f"Last occurrence of \"a\" in the first word: {string.rfind("a")}")
