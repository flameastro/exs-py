# ex039: Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
numeros = []
alturas = []
for i in range(10):
    numero_aluno = int(input("Digite o número do aluno: "))
    if numero_aluno in numeros:
        print("Este número de aluno já foi cadastrado. Considere-se inserir outro número.")
        numero_aluno = int(input("Digite o número do aluno: "))

    altura = float(input("Digite a altura do aluno: "))

    numeros.append(numero_aluno)
    alturas.append(altura)

altura_mais_alto = max(alturas)
altura_mais_baixo = min(alturas)
numero_mais_alto = numeros[alturas.index(altura_mais_alto)]
numero_mais_baixo = numeros[alturas.index(altura_mais_baixo)]

print(f"O aluno com a maior altura possui {altura_mais_alto}cm e tem o número {numero_mais_alto}")
print(f"O aluno com a menor altura possui {altura_mais_baixo}cm e tem o número {numero_mais_baixo}")
