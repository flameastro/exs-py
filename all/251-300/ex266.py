# ex266: When provided with a letter, return its position in the alphabet.
# Input :: "a"
# Output :: "Position of alphabet: 1"
def position(letter):
    return f"Position of alphabet: {ord(letter.upper()) - 64}"


if __name__ == "__main__":
    print(position("a"))  # Position of alphabet: 1
    print(position("b"))  # Position of alphabet: 2
    print(position("z"))  # Position of alphabet: 26
