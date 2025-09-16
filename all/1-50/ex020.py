# ex020: Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
nome = input('Digite o seu nome: ').strip().title()
n1 = float(input(f'{nome}, Digite a primeira nota: '))
n2 = float(input(f'{nome}, Digite a segunda nota: '))

media = (n1 + n2) / 2

if media > 7.0:
    print('Você está aprovado')
elif media > 5.0:
    print('Você está em recuperação')
else:
    print('Você está reprovado')
