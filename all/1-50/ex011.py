# ex011: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$6.
reais = int(input('Quantos reais você tem? '))
dolares = reais / 6

print(f'Você pode comprar {round(dolares, 2)} doláres.')
