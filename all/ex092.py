# ex092: Inverta o exercício 11 - imprima uma escada de estrelas invertidas
def piramide_de_estrelas(quantidade: int):
    if quantidade < 1 or quantidade > 100:
        print("A quantidade deve estar entre 1 a 100.")
        return None

    for numero in range(quantidade, 0, -1):
        print("*" * numero)


quantidade = int(input("Digite a quantidade de 1 a 100:\n>>> "))
piramide_de_estrelas(quantidade)
