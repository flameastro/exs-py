# ex105: Faça um programa que leia um número menor que 1000 e imprima centenas, dezenas e unidades.

def decomposicao(numero: int) -> str:
    if numero < 1 or numero >= 1000:
        return "O número deve ser maior ou igual a 1 e menor que 1000"

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    return f"Centenas: {centenas} | Dezenas: {dezenas} | Unidades: {unidades}"


def main():
    try:
        numero = int(input("Digite um número entre 1 e 999: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    print(decomposicao(numero))


if __name__ == "__main__":
    main()
