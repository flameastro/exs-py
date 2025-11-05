# ex010: Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
from random import randint
def jogo_de_craps():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2

    print(f"Resultado do dado 1: {dado1}")
    print(f"Resultado do dado 2: {dado2}")
    print(f"Soma: {soma}")

    if soma == 7 or soma == 11:
        print("Natural -> Ganhou")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Craps -> Perdeu")
    elif soma in range(4, 7) or soma in range(8, 11):
        print("Ponto")

jogo_de_craps()
