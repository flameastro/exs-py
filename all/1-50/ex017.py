# ex017: [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
cigarros_dia = int(input('Quantos cigarros fuma por dia? '))
anos = int(input('Quantos anos fuma? '))

total_cigarros = cigarros_dia * 365 * anos
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 60 / 24

print(f'Dias perdidos: {dias_perdidos}')
