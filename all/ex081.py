# ex081: Faça um algoritmo que leia a nota de vários alunos de uma turma. O programa vai parar quando for digitada a nota 999. No final, mostre quantos alunos existem na turma e qual é a média de notas do grupo.

notas = []
alunos = 0
while True:
    nota = int(input(f'Digite a nota do aluno [999 = sair]: '))
    while nota < 0 or nota > 10 and nota != 999:
        nota = int(input(f'Digite corretamente [999 = sair]: '))
    if nota == 999:
        break



    alunos += 1
    notas.append(nota)

if len(notas) > 1:
    media = sum(notas) / len(notas)
    print(f'Nessa turma, existem {alunos} alunos')
    print(f'A média de notas da turma é de {media}')
