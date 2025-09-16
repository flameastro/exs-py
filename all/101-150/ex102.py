# ex102: # Faça um aplicativo onde o computador deve sortear um número entre 1 e 10 e o jogador tem 4 tentativas para tentar acertar
from random import randint

computador = randint(1, 10)

for i in range(4):
    print(f'⏳Tentativa {i+1}/4⏳'.center(50, '-'))

    escolha = int(input('Tente adivinhar o número entre 1 a 10: '))
    while escolha <= 0 or escolha > 10:
        escolha = int(input('❓Por favor, escolha um número entre 1 a 10❓: '))
    
    if escolha == computador:
        print('🎇 Você acertou!🎇')
        break
    else:
        if i == 3:
            print(f'🎈O número era {computador}🎈')
        else:
            print('❌ Você errou. Tente novamente❌')
