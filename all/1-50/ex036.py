# ex036: Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m2. O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m2 = TERRENO POPULAR
# - Entre 100m2 e 500m2 = TERRENO MASTER
# - Acima de 500m2 = TERRENO VIP

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area = largura * comprimento

if area > 500:
    print('Terreno VIP')
elif area < 500 and area > 100:
    print('Terreno MASTER')
elif area < 100:
    print('Terreno POPULAR')
