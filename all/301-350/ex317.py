# ex317: Escreva um algoritmo que calcule e exiba a tabuada, até um determinado número “n”, fornecido pelo usuário, lembrando que, se o número fornecido é 4, deve ser gerada a tabuada do 1, 2, 3 e 4, com as operações de multiplicação e o resultado no formato:
# 1x1 = 1
# 1x2 = 2
# 1x3 = 3
# ...
n = int(input("Digite um número inteiro e positivo: "))

if n > 0:
    for i in range(1, n+1):
        print(f"1x{i} = {1 * i}")
else:
    print("O número inserido deve ser maior que 0")
