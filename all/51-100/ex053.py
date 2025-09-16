# ex053: Crie uma função que recebe um número e imprima o seu dobro.
def dobro(numero: int):
    if numero < 1 or numero > 10000000:
        return "O número deve estar entre 1 e 10mi."
    dobro = numero * 2
    return f"O dobro de {numero} é {dobro}"


if __name__ == "__main__":
    print(dobro(15))
    print(dobro(25))
