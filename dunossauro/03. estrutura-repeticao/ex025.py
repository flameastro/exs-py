# ex025: Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
soma = 0
quantidade = 0

while True:
    idade = int(input("Insira a sua idade: "))

    while idade not in range(0, 121):
        print("Por favor, considere inserir uma idade válida.")
        idade = int(input("Insira a sua idade: "))

    soma += idade
    quantidade += 1

    continuar = input("Deseja continuar? [S/N] ").upper().strip()
    while continuar not in ["S", "N"]:
        print("Por favor, certifique-se de inserir S para SIM e N para NÃO")
        continuar = input("Deeseja continuar? [S/N] ").upper().strip()

    if continuar == "N":
        break


media = soma / quantidade

if media >= 0 and media <= 25:
    print("A média varia entre 0 a 25 - Turma Jovem")
elif media > 25 and media <= 60:
    print("A média varia entre 26 a 60 - Turma Adulta")
elif media > 60:
    print(f"A média varia dos 60+ - Turma Idosa")

