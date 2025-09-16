# ex220: Efetuar a leitura de três valores inteiros desconhecidos representados pelas variáveis A, B e C. Somar os valores fornecidos e apresentar o resultado somente se for maior ou igual a 100.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

soma = A + B + C

if soma >= 100:
    print("A soma é maior ou igual a 100.")
else:
    print("A soma está abaixo de 100.")
