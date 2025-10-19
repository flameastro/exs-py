# ex023: Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero = float(input("Digite um número qualquer: "))

if numero.is_integer():
    print("INTEIRO")
else:
    print("DECIMAL")
