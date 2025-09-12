# ex010: Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
metros = float(input('Digite uma distância em metros: '))
print(f'{metros / 1000}Km')
print(f'{metros / 100}Hm')
print(f'{metros / 10}Dam')
print(f'{metros * 10}dm')
print(f'{metros * 100}cm')
print(f'{metros * 1000}mm')
