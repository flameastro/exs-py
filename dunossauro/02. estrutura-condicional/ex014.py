# ex014: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero         E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input("Digite a sua primeira nota: "))
while nota1 not in range(0, 11):
    print("Por favor, insira uma nota válida.")
    nota1 = float(input("Digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))
while nota2 not in range(0, 11):
    print("Por favor, insira uma nota válida.")
    nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media >= 0 and media < 4:
    conceito = "E"


print(f"A primeira nota foi {nota1}")
print(f"A segunda nota foi {nota2}")
print(f"A média das notas é {media}")
print(f"O conceito é {conceito}")
print(f"Você foi... {'APROVADO' if conceito in ["A", "B", "C"] else 'REPROVADO'}")
