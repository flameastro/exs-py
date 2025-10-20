# ex035: Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
numero = int(input("Insira um número inteiro: "))

divisores = [divisivel for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(divisores)
else:
    print(f"{numero} não possui divisores, é um número primo.")

