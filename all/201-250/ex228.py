# ex228: Criar uma aplicação que pergunte dois números inteiros. Se não forem iguais, sorteie 0 ou 1. Se for 0, o menor número ganha. Mas se for 1, ganha o maior número.
from random import randint

jogador1 = int(input("Digite o valor de A: "))
jogador2 = int(input("Digite o valor de B: "))

if jogador1 != jogador2:
    numero = randint(0, 1)
    print(f"Número sorteado: {numero}")

    if (numero == 0 and jogador1 < jogador2) or (numero == 1 and jogador1 > jogador2):
        print("Jogador 1 Ganhou!")
    else:
        print("Jogador 2 Ganhou!")
else:
    print(f"Empate")
