# ex233: Sorteie um número entre 1 e 10 e peça ao usuário para tentar adivinhá-lo. Quando o usuário acertar o número, informe quantas tentativas foram necessárias.
from random import randint

numero = randint(1, 10)
tentativas = 0

while True:
    escolha = int(input("Tente acertar um número de 1 a 10: "))
    while escolha not in range(1, 11):
        escolha = int(input("Por favor, digite corretamente.\nTente acertar um número de 1 a 10: "))

    if escolha == numero:
        print(f"Tentativas necessárias: {tentativas}")
        break
    else:
        print("Tente novamente.")
        tentativas += 1
