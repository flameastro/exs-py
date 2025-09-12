# ex079: Desenvolva um aplicativo que leia o peso e a altura de 5 pessoas, mostrando no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg e tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m e pesam mais de 100Kg.

alturas = []
mais90 = peso50_alt160 = peso100_alt190 = 0
for i in range(5):
    peso = float(input(f'Digite o peso da pessoa {i+1}: '))
    altura = float(input(f'Digite a altura da pessoa {i+1}: '))

    alturas.append(altura)

    if peso > 90:
        mais90 += 1
    
    if peso < 50 and altura < 1.60:
        peso50_alt160 += 1
    
    if peso > 100 and altura > 1.90:
        peso100_alt190 += 1


media = sum(alturas) / len(alturas) / 10

print(f'A média das alturas é de {media}')
print(f'Há {mais90} {"pessoa que pesa" if mais90 == 1 else "pessoas que pesam"} mais de 90 quilos')
print(f'Há {peso50_alt160} {"pessoa que pesa" if peso50_alt160 == 1 else "pessoas que pesam"}  menos de 50 quilos e tem menos de 1.60m')
print(f'Há {peso100_alt190} {"pessoa que pesa" if peso100_alt190 == 1 else "pessoas que pesam"} mais de 100 quilos e tem mais de 1.90m')
