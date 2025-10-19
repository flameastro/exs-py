# ex017: Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
numero = int(input("Insira o número que deseja descobrir o fatorial: "))
fatorial = 1

for i in range(1, numero+1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial} ({"x".join([str(x) for x in range(numero, 0, -1)])} = {fatorial})")
