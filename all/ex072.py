# ex072: Crie um jogo de JoKenPo (Pedra-Papel-Tesoura) com o computador
from random import randint
computador = randint(1, 3)
escolha = input('pedra, papel ou tesoura? ').strip().lower()

computador = 'pedra' if computador == 1 else 'papel' if computador == 2 else 'tesoura'
print(f'A máquina escolheu {computador}')   

empate = computador == escolha

vitoria = (computador == "pedra" and escolha == "papel") or (computador == "papel" and escolha == "tesoura") or (computador == "tesoura" and escolha == "pedra")

derrota = (computador == "pedra" and escolha == "tesoura") or (computador == "papel" and escolha == "pedra") or (computador == "tesoura" and escolha == "papel")

print('Empate' if empate else 'Você ganhou! A máquina perdeu' if vitoria else 'Você perdeu! A máquina ganhou' if derrota else 'Escolha inválida! Digite "pedra", "papel" ou "tesoura"')
