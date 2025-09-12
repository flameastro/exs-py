# ex076: Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
from datetime import datetime
nascimento = int(input('Digite a sua data de nascimento: '))

ano = datetime.now().year
idade = ano - nascimento

if idade >= 18:
    print('Você pode votar')
else:
    print(f'Você não pode votar, pois tem {idade} anos')
