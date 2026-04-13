# ex315: Um aluno realizou três provas de uma determinada disciplina. Levando em consideração o critério apresentado a seguir, faça um programa que mostre se ele ficou para exame e, em caso positivo, que nota este aluno precisa obter, no exame, para passar de ano.
# Média = (nota1 + nota2 + nota3) / 3
# A média deve ser maior ou igual a 7,0. Se não conseguir, a nova média deve ser:
# Final = (Média + Exame) / 2
# A média final, para aprovação, deve ser maior ou igual a 5,0.
nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print(f"Sua média: {media}")
if media >= 7:
    print("Aprovado")
else:
    print(f"Você ficou em recuperação, faltando {7 - media} pontos para passar. faça um exame de recuperação.")

    exame = float(input("Insira a nota do exame: "))
    final = (media + exame) / 2
    print(f"Sua nota final: {final}")

    if final >= 5:
        print("Aprovado")
    else:
        print("Reprovado")
        print(f"Poxa! Faltaram {5 - media} pontos para passar")
