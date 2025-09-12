# ex052: Crie uma função que recebe um número e imprima seu sucessor e seu antecessor
def sucessor_antecessor(numero: int):
    if numero < 1 or numero > 10000000:
        return "O número deve estar entre 1 e 10mi."

    sucessor = numero + 1
    antecessor = numero - 1

    return f"O número sucessor é {sucessor} e o número antecessor é {antecessor}"


if __name__ == "__main__":
    print(sucessor_antecessor(15))
    print(sucessor_antecessor(23))
    print(sucessor_antecessor(1))
    print(sucessor_antecessor(9999999))
