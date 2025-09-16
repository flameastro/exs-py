# ex150: Crie uma função que inverta uma string
def invert_string(string: str):
    if not isinstance(string, str) or len(string) <= 1:
        return "String inválida, preencha corretamente."

    letters = len(string)
    inversed_string = ""

    for letter in range(letters):
        last_letter = string[-letter-1]
        inversed_string += last_letter

    return inversed_string


if __name__ == "__main__":
    print(invert_string("Flame"))  # emalF
    print(invert_string("Python"))  # nohtyp
    print(invert_string("subi no onibus"))  # subino on ibus

    string = input("Por favor, digite a string que queira inverter:\n>>> ")
    print(invert_string(string))
