# ex139: Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula: distância = sqrt((x2 - x1)^2 + (y2 - y1)^2). O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2. Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.
from math import sqrt

x1 = float(input("Valor do x1:\n>>> "))
y1 = float(input("Valor do y1:\n>>> "))

x2 = float(input("Valor do x2:\n>>> "))
y2 = float(input("Valor do y2:\n>>> "))

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")
