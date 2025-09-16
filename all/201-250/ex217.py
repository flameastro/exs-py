# ex217: Fazer a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D. Apresentar apenas os valores que sejam divisíveis por 2 e 3.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

for n in [A, B, C, D]:
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} é divisível por 2 e por 3.")
