# ex016: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = int(input("Digite o tamanho da área em metros quadrados: "))

cobertura = area / 3
latas = cobertura / 18
preco = latas * 80

print(" Detalhes ".center(25, "-"))
print(f"Área: {area:.2f}")
print(f"Cobertura: {cobertura:.2f} litros")
print(f"Latas: {latas:.2f}")
print(f"Preço: {preco:.2f}")
