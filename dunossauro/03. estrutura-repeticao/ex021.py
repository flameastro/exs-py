# ex021: Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero = int(input("Insira um número inteiro: "))

divisores = [divisivel for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(f"{numero} não é um número primo (número composto)")
else:
    print(f"{numero} é um número primo.")
