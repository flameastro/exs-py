# ex044: Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados.

vetor = [[], [], [], [], [], [], []]

for i in range(7):
    pessoa = input('Digite o nome da pessoa: ')
    vetor[i] = pessoa

vetor.reverse()
print(vetor)
