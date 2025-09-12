# ex026: Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km

carro = input('Qual o tipo de carro? [popular/luxo]: ').strip().lower()
dias = int(input('Quantos dias? '))
kms = float(input('Quantos kms percorridos? '))

if carro == 'popular':
    aluguel = dias * 90
    if kms > 100:
        aluguel += kms * 0.10
    else:
        aluguel += kms * 0.20
elif carro == 'luxo':
    aluguel = dias * 150 
    if kms > 200:
        aluguel += kms * 0.25
    else:
        aluguel += kms * 0.30
else:
    print('Carro não encontrado.')

print(f'O aluguel do carro está com o preço de R${aluguel:.2f}')
