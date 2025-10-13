# ex279: Crie um programa que peça ao usuário digitar o valor do numerador e denominador e imprima a fração em decimal.
numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))

fracao = numerador / denominador
print(f"O valor decimal da fração é {fracao}")
