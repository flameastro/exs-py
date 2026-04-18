# ex336: Construa um programa que tem como dados de entrada dois pontos quaisquer no plano cartesiano: P1 e P2. Considere que P1 é definido pelas coordenadas x1 e y1, enquanto P2 por x2 e y2 . O programa deve calcular e escrever a distância entre os pontos P1 e P2. A fórmula que calcula a distância entre os dois pontos é dada por:
# d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
from math import sqrt


x1 = int(input("Digite o valor da coordenada x1: "))
y1 = int(input("Digite o valor da coordenada y1: "))
x2 = int(input("Digite o valor da coordenada x2: "))
y2 = int(input("Digite o valor da coordenada y2: "))

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"A distância entre os pontos é: {d}")
