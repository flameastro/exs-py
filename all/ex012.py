# ex012: Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))

area = largura * altura
tinta = area / 2

print(f'A área da parede é de {area}m²')
print(f'A tinta necessária é {tinta} litros de tinta')
