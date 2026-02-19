# ex296: Count all letters, digits, and special symbols from a given string
# Given:
# str1 = "P@#yn26at^&i5ve"

# Expected Outcome:
# Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbols = 4
def divide_characters(string):
    chars = 0
    digits = 0
    symbols = 0

    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_digits = "0123456789"

    for l in string:
        if l in all_characters:
            chars = chars + 1
        elif l in all_digits:
            digits = digits + 1
        else:
            symbols = symbols + 1

    return f"Chars = {chars}\nDigits = {digits}\nSymbols = {symbols}"


if __name__ == "__main__":
    print(divide_characters("P@#yn26at^&i5ve"))  # Chars = 8 | Digits = 3 | Symbols = 4
    print(divide_characters("MyP@ssword123"))  # Chars = 9 | Digits = 3 | Symbols = 1
    print(divide_characters("Hello, World!"))  # Chars = 10 | Digits = 0 | Symbols = 3
