# ex069: Crie uma função que recebe um texto e uma letra e verifica quantas vezes essa letra está presente no texto
def conta_letras(texto: str, letra: str):
    if len(letra) == 1:
        if letra in texto:
            contagem = texto.count(letra)
            return f"A letra aparece {contagem} vezes no texto."

        return "A letra não aparece no texto."

    return "A letra deve conter apenas um caractere."


if __name__ == "__main__":
    print(conta_letras("Python", "o"))  # A letra aparece 1 vez no texto.
    print(conta_letras("JavaScript", "a"))  # A letra aparece 2 vezes no texto.
    print(conta_letras("Branco", "Z"))  # A letra não aparece no texto.
    print(conta_letras("Amazônia", "ama"))  # A letra deve conter apenas um caractere.
