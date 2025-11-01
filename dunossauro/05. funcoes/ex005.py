# ex005: Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas.
def soma_imposto(custo: float, taxa_imposto: float):
    return custo - (custo * taxa_imposto)


if __name__ == "__main__":
    print(soma_imposto(1250.99, 0.4))  # 750.594
    print(soma_imposto(25350, 0.15))  # 21547.5
    print(soma_imposto(785.8, 0.45))  # 432.18999999999994
