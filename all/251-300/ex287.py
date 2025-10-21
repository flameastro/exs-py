# ex287: O diretor de uma escola precisa da sua ajuda. Ele não sabe exatamente qual o número total de estudantes da escola toda, mas ele sabe que existem 12 salas de aula. Ele preencheu 35 alunos em cada sala, e sobraram 7 alunos. Quantos alunos há naquela escola? Crie um programa que calcule o total de alunos que essa escola possui.
salas = 12
alunos_por_sala = 35

alunos = (alunos_por_sala * salas) + 7
print(f"Há aproximadamente {alunos} alunos nessa escola.")  # Há aproximadamente 427 alunos nessa escola.
