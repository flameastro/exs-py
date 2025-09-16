# ex196: In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.
# Example
# Input = "The sunset sets at twelve o' clock." -> "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
def alphabet_position(text):
    alphabet = ['.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return " ".join([str(alphabet.index(x)) for x in text.lower() if x.isalpha()])


if __name__ == "__main__":
    print(alphabet_position("The sunset sets at twelve o' clock."))  # 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
    print(alphabet_position("Jorge is going to launch"))  # 10 15 18 7 5 9 19 7 15 9 14 7 20 15 12 1 21 14 3 8
    print(alphabet_position("Hikaru buys a porsche and play chess while driving"))  # 8 9 11 1 18 21 2 21 25 19 1 16 15 18 19 3 8 5 1 14 4 16 12 1 25 3 8 5 19 19 23 8 9 12 5 4 18 9 22 9 14 7
