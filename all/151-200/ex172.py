# ex172: Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained. Examples "This is an example!" ==> "sihT si na !elpmaxe"; "double  spaces"      ==> "elbuod  secaps"
def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])

    # or
    #     string = []

    #     for word in text.split(" "):
    #         string.append(word[::-1])

    #     return " ".join(string)


if __name__ == "__main__":
    print(reverse_words("This is an example!"))  # sihT si na !elpmaxe
    print(reverse_words("a b c d"))  # a b c d
    print(reverse_words("double  spaces"))  # elbuod  secaps
