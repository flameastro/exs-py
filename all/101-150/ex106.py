# ex106: Crie uma função que tem uma string como parâmetro e verifica se a string é um palíndromo.
def verifica_palindromo(string: str):
    try:
        if len(string) < 1:
            return "A string deve ter ao mínimo 1 caractere."

        if string[::-1].lower() == string.lower():
            return "A string é um palíndromo."
    except TypeError as type_e:
        return f"A string deve conter apenas letras. Erro: {type_e}"
    except Exception as e:
        return f"Erro: {e}"

    return "A string não é um palíndromo."


if __name__ == "__main__":
    print(verifica_palindromo("radar"))  # A string é um palíndromo.
    print(verifica_palindromo("Ana"))  # A string é um palíndromo.
    print(verifica_palindromo(""))  # A string deve ter ao mínimo 1 caractere.
    print(verifica_palindromo(12345))  # A string deve ter ao mínimo 1 caractere.
