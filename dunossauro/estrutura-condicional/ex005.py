# ex005: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input("Digite a primeira nota: "))
while nota1 not in range(0, 11):
    print("Por favor, certifique-se de inserir uma nota válida.")
    nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 not in range(0, 11):
    print("Por favor, certifique-se de inserir uma nota válida.")
    nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Oops, algo deu errado! Por favor, tente novamente.")
