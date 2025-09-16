# ex155: Crie uma função que receba uma lista de números como parâmetro e retorne cada valor com a sua operação trocada (positivos viram negativos e vice-versa).
def inverte_operacoes(lista: list):
    lista_operacoes_inversa = []

    for valor in lista:
        if valor > 0:
            lista_operacoes_inversa.append(-valor)
        else:
            lista_operacoes_inversa.append(abs(valor))

    return lista_operacoes_inversa

if __name__ == "__main__":
    print(inverte_operacoes([12, -3, 50, -15]))  # [-12, 3, -50, 15]
    print(inverte_operacoes([0, 12, -7, 999, 4]))  # [0, -12, 7, -999, -4]
    print(inverte_operacoes([56, 12, 3, -9, 15]))  # [-56, -12, -3, 9, -15]
