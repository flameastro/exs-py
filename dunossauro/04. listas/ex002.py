# ex002: Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
for x in range(10):
    vetor.append(int(input("Insira um número: ")))

print(list(reversed(vetor)))
