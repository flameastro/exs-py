# ex006: Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias = []

for aluno in range(10):
    notas = []

    for n in range(4):
        nota = float(input(f"Digite a nota do aluno {aluno+1}: "))
        while nota < 0 or nota > 10:
            print("Por favor, considere inserir uma nota válida.")
            nota = float(input(f"Digite a nota do aluno {aluno+1}: "))

        notas.append(nota)

    media = sum(notas) / 4
    medias.append(str(media))

aprovados = len([x for x in medias if float(x) >= 7])
print(f"O número de alunos com média superior a 7 é {aprovados}.")
