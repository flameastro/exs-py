# ex028: Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
quantidade_cds = int(input("Quantos CDs o colecionador possui? "))
while quantidade_cds not in range(1, 1001):
    print("Por favor, considere inserir uma quantidade válida.")
    quantidade_cds = int(input("Quantos CDs o colecionador possui? "))

total = 0

for cd in range(quantidade_cds):
    valor = float(input(f"Qual foi o valor em reais gasto pelo CD {cd+1}? R$"))
    while valor not in range(0, 10**9):
        print("Por favor, considere inserir um valor válido.")
        valor = float(input(f"Qual foi o valor em reais gasto pelo CD {cd+1}? R$"))

    total += valor

media = total / quantidade_cds

print(f"A média dos valores dos cds em reais é R${media:.2f}")
