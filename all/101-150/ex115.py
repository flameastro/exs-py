# ex115: Faça uma função que conta o número de vogais em uma string.
def count_vowels(string: str):
    if len(string) < 1 or len(string) > 250:
        return "O tamanho da string deve estar entre 1 a 250."

    try:
        VOWELS = ["a", "e", "i", "o", "u"]

        count = 0
        for letter in string.lower():
            if letter in VOWELS:
                count += 1

        return count
    except ValueError as value_e:
        return f"Erro de valor: {value_e}"
    except KeyboardInterrupt as keyboard_e:
        return f"Erro de teclado: {keyboard_e}"
    except TypeError as type_e:
        return f"Erro de tipo: {type_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(count_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # 5
    print(count_vowels("Existe uma cobra chamada Python."))  # 11
    print(count_vowels("Eistein é o maior cientista de todos os tempos."))  # 18
    print(count_vowels(""))  # O tamanho da string deve estar entre 1 a 250.
    print(count_vowels("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Provident facilis sequi voluptas, veritatis quaerat id repellendus blanditiis quo corporis, quis tempore obcaecati amet? Error, qui! Quam quidem consectetur tempore inventore? Placeat, saepe atque natus recusandae neque porro vel repellendus inventore molestiae ut?"))  # O tamanho da string deve estar entre 1 a 250.
