# ex123: Faça um simulador de dado
from random import randint


def simular_dado(quantidade: int):
    if quantidade > 10000 or quantidade < 1:
        yield "A quantidade de tentativas deve ser menor que 10000 e maior que 0."
        return None

    resultados = []
    for _ in range(quantidade):
        dado = randint(1, 6)

        resultados.append(dado)

    for i in range(1, 7):
        yield f"Dado caiu em {i}: {resultados.count(i)} vezes."

    yield f"Resultados: {resultados}"


try:
    quantidade = int(input("Digite a quantidade de vezes para sortear o dado:\n>>> "))
except ValueError:
    print("Valor inválido. Digite um número!")
except Exception as erro:
    print(f"Erro: {erro}")
else:
    for item in simular_dado(quantidade):
        print(item)
