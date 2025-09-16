# ex101: Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
from random import randint

computador = randint(1, 5)
escolha = int(input('Tente adivinhar o número entre 1 a 5: '))

while escolha <= 0 or escolha > 5:
    escolha = int(input('Por favor, escolha um número entre 1 a 5: '))

print(f'Você acertou' if escolha == computador else f'Você errou, o número era {computador}')
