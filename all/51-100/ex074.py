# ex074: Faça um programa que simule o lançamento de dois dados e exiba o resultado da soma.
from random import randint

def simulacao_dado():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    resultado = dado1 + dado2
    print(f'O resultado do dado 1 ({dado1}) com o dado 2 ({dado2}) é {resultado}')


simulacao_dado()
