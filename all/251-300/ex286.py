# ex286: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#     Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math


A = int(input("Digite o valor de A: "))
if A == 0:
    print("O valor de A não pode ser 0.")
else:
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))

    DELTA = B ** 2 - 4 * A * C
    if DELTA < 0:
        print("A equação não possui raízes reais.")
    elif DELTA == 0:
        print("A equação possui apenas uma raiz real.")
    else:
        print("A equação possui duas raiz reais.")

        x = {(-B + math.sqrt(DELTA)) / (2 * A), (-B - math.sqrt(DELTA)) / (2 * A)}
        print(f"O valor de DELTA é {DELTA}")
        print(f"O Conjunto solução é {x}")
