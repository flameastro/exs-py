# ex095: Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo computador e depois mostre os valores gerados na tela.
import random

vetor = [[], [], [], [], [], [], []]

for i in range(7):
    vetor[i] = random.randint(1, 10)

print(vetor)
