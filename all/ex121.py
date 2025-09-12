# ex121: Crie um programa que simule um jogo de "cara ou coroa" com estatísticas de vitórias.
from random import randint


def cara_ou_coroa(quantidade: int):
    if quantidade > 100 or quantidade < 1:
        return "A quantidade de tentativas deve ser menor que 100 e maior que 1."

    resultados = []
    for _ in range(quantidade):
        moeda = randint(0, 1)

        if not moeda:
            resultados.append("Cara")
        else:
            resultados.append("Coroa")

    return (
        f"Resultados: {", ".join(resultados)}\n"
        f"Qntd. de vezes que caiu Cara: {resultados.count("Cara")}\n"
        f"Qntd. de vezes que caiu Coroa: {resultados.count("Coroa")}\n"
    )


quantidade = int(input("Quantas vezes deseja jogar?\n>>> "))
print(cara_ou_coroa(quantidade))
