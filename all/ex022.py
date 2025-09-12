# ex022: Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO. (formula básica)
ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('Ano é Bissexto')
else:
    print('Ano não é Bissexto')
