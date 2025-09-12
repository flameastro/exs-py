# ex013: Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
produto = float(input('Digite o preço do produto: '))
desconto = produto * 0.05
preco = produto - desconto

print(f'O preço do produto com um desconto de 5% é de {preco}')
