# ex261: Write a program that replaces all instances of ”one” with ”one (1)”. For this exercise, capitalization does not matter, so it should treat ”one”, ”One”, and ”oNE” identically.
string = input("Type a string: ")

print(f"{string.lower().replace("one", "one (1)")}")
