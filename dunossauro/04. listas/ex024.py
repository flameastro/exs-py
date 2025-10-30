# ex024: Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
import random

def lancar_dado():
    return random.randint(1, 6)

resultados = []
contadores = [0] * 6

for _ in range(100):
    resultado = lancar_dado()
    resultados.append(resultado)
    contadores[resultado - 1] += 1

print("Resultados dos lançamentos:")
for i in range(6):
    print(f"{i + 1}: {contadores[i]} vezes")
