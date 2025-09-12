# ex034: A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159. Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
from math import pi

raio = float(input('Digite o valor do raio: '))
area = (raio ** 2) * pi

print(f'A área do círculo é {round(area, 4)}')
