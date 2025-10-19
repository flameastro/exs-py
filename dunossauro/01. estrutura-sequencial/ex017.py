# ex017: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
area = int(input("Digite o tamanho da área em metros quadrados: "))
cobertura = area / 6

latas = cobertura / 18
preco_latas = latas * 80

galoes = cobertura / 3.6
preco_galoes = galoes * 25

print(" Detalhes ".center(25, "-"))
print(f"Cobertura: {cobertura:.2f} litros")
print("Comprando em Latas:")
print(f"Latas: {latas:.2f}")
print(f"Preço: {preco_latas:.2f}")
print("Comprando em Galões:")
print(f"Galões: {galoes:.2f}")
print(f"Preço dos Galões: {preco_galoes:.2f}")
