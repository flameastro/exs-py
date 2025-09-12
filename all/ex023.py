# ex023: Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas.
distancia = int(input('Quantos Kms deseja percorrer? '))

if distancia < 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço final é de R${preco} reais')
