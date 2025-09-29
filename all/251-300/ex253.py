# ex253: Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times

def duplicate_count(text):
    letters = []

    for string in text.lower():
        if string not in letters and text.lower().count(string) > 1:
            letters.append(string)

    return len(letters)


if __name__ == "__main__":
    print(duplicate_count("abcdeaB"))
    print(duplicate_count("Wm18tVKzlsW6uPYCy6JAvsss5Y642VLxKOJcTPqcsb"))
