# ex332: Crie um programa de MEGA-SENA: O usuário deve digitar um número N, e o programa deve apresentar N quantidade de jogos da mega-sena com 6 números cada jogo. Cada jogo deve ter números aleatórios e em ordem crescente.
# Importa bibliotecas para tempo e números aleatórios
from random import randint as random
from time import sleep as time


print("BEM VINDO")
print("--- M E G A    S E N A ---")

jogos = int(input("Quantos Jogos da Mega Sena deseja? "))

for j in range(jogos):
    jogo = []  # Reseta o array jogo a cada repetição

    for numero in range(6):
        palpite = random(1, 60)

        # Repete o palpite enquanto esse já estiver contindo no array jogo
        while palpite in jogo:
            palpite = random(1, 60)

        jogo.append(palpite)

    # Ordena o array jogo
    jogo = list(sorted(jogo))

    print(f"Jogo {j+1}: {jogo}")
    time(0.25)  # Espera 0.250 segundos para cada jogo
