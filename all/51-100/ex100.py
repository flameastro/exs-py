# ex100: Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.

from datetime import datetime
nascimento = int(input('Digite a sua data de nascimento: '))

ano = datetime.now().year
idade = ano - nascimento

if idade < 18:
    falta = 18 - idade
    print(f'Faltam {falta} anos')
else:
    passou = idade - 18
    print(f'Já se passou {passou} anos')
