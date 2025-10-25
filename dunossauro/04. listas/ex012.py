# ex012: Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = []
alturas = []

for aluno in range(30):
    idade = int(input("Idade: "))
    while idade not in range(0, 80):
        print("Por favor, insira um valor adequado.")
        idade = int(input("Idade: "))

    altura = float(input("Altura: "))
    while altura < 0 or altura > 3:
        print("Por favor, digite um valor para a altura que seja válido.")
        altura = float(input("Altura: "))

    idades.append(idade)
    alturas.append(altura)

media = sum(alturas) / 30
altura_inferior = 0

for i in range(30):
    if idades[i] > 13 and alturas[i] < media:
        altura_inferior += 1

print(f"A quantidade total de alunos que possui mais de 13 anos e há uma altura inferior em relação à média é de: {altura_inferior}")
