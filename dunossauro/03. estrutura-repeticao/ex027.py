# ex027: Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
turmas = int(input("Insira a quantidade de turmas:\n>>> "))
while turmas not in range(1, 25):
    print("Considere inserir um valor entre 1 a 25 turmas.")
    turmas = int(input("Insira a quantidade de turmas:\n>>> "))

total = 0

for turma in range(turmas):
    alunos = int(input(f"Quantos alunos há na turma {turma+1}?\n>>> "))
    while alunos not in range(10, 41):
        print("⚠️ A turma deve possui entre 10 a 40 alunos.")
        alunos = int(input(f"Quantos alunos há na turma {turma+1}?\n>>> "))

    total += alunos

media = total / turmas

print(f"A média de alunos por turma é de {media:.2f}")
