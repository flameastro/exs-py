# ex096: Crie uma uma função que retorne a maior palavra de uma string.
def biggest_word(text: str):
    if len(text) < 1 or len(text) > 10000:
        return "Texto inválido."

    words = text.split()

    lenghts = list(map(len, words))
    position = lenghts.index(max(lenghts))

    word = words[position]
    return word


if __name__ == "__main__":
    print(biggest_word(""))  # Texto inválido.
    print(biggest_word("# a b c d"))  # #
    print(biggest_word("Tor is the best anonymous and security browser")) # anonymous
