# ex193: Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!
# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
def smash(words):
    return " ".join(words)


if __name__ == "__main__":
    print(smash(["Hello", "World!"]))  # Hello World!
    print(smash(["flame", "astro"]))  # flame astro
