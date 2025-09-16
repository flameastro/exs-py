# ex154: Crie uma função que receba uma lista e retorne a soma de todos os valores positivos.
def soma_positivos(lista: list) -> int:
    soma = 0

    for valor in lista:
        if valor > 0:
            soma += valor

    return soma


if __name__ == "__main__":
    print(soma_positivos([12, -5, 12, -3, 0, -9]))  # 24
    print(soma_positivos([40, 10, -50, 0, 90]))  # 140
    print(soma_positivos([-5, -3, -15, -999]))  # 0
