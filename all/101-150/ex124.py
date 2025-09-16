# ex124: Crie uma função que conta quantas letras há numa string.
def count_letters(text):
    already_list = []

    for letter in text:
        if letter.isalpha():
            if letter not in already_list:
                already_list.append(letter)
                print(f"{letter}: {text.count(letter)}")

if __name__ == "__main__":
    count_letters("Contador de Letras com Python!")
    count_letters("JavaScript ou Python?")
    count_letters("AAA BBB CCC DDD EEE")
