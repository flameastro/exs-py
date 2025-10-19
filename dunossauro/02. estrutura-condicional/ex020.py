# ex020: Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
n1 = float(input("Digite a primeira nota: "))
while n1 not in range(0, 11):
    print("Nota inválida, por favor, insira novamente.")
    n1 = float(input("Digite a primeira nota: "))

n2 = float(input("Digite a segunda nota: "))
while n2 not in range(0, 11):
    print("Nota inválida, por favor, insira novamente.")
    n2 = float(input("Digite a segunda nota: "))

n3 = float(input("Digite a terceira nota: "))
while n3 not in range(0, 11):
    print("Nota inválida, por favor, insira novamente.")
    n3 = float(input("Digite a terceira nota: "))

media = (sum[n1, n2, n3]) / 3
print(f"Média: {media}")

if media == 10:
    print("APROVADO COM DISTINÇÃO")
if media >= 7:
    print("APROVADO")
elif media < 7:
    print("REPROVADO")
