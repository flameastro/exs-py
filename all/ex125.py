# ex125: Crie uma função que conta quantas palavras há numa string.
def count_words(text):
    splitted_text = text.split()
    already_list = []

    for element in splitted_text:
        if element not in already_list:
            already_list.append(element)
            print(f"{element}: {splitted_text.count(element)}")

if __name__ == "__main__":
    count_words("Hello world! Hello Python!")
    count_words("Olá mundo! Olá Python!")
