# ex016: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Isso não é uma equação do segundo grau.")
else:
    DELTA = (b ** 2) * -4 * a * c

    if DELTA < 0:
        print(f"A equação não possui raízes reais.")
    elif DELTA == 0:
        print(f"A equação possui apenas uma raíz real.")
    else:
        print(f"A equação possui duas raízes reais.")
        conjunto = {(-b + sqrt(DELTA)) / (2 * a), (-b - sqrt(DELTA)) / (2 * a)}

        for x in conjunto:
            print(x)
