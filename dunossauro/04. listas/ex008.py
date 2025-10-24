# ex008: Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []

for x in range(5):
    idade = int(input("Idade: "))
    while idade not in range(0, 121):
        print("Por favor, insira um valor adequado.")
        idade = int(input("Idade: "))

    altura = float(input("Altura: "))
    while altura < 0 or altura > 3:
        print("Por favor, digite um valor para a altura que seja válido.")
        altura = float(input("Altura: "))

    idades.append(idade)
    alturas.append(altura)


print(idades[::-1])
print(alturas[::-1])

