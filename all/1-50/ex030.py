# ex030: Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:
# Ex: Digite o primeiro Valor: 3
# Digite o último Valor: 10
# Digite o incremento: 2
# Contagem: 3 5 7 9 Acabou!
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passos = int(input('Digite os passos: '))

for i in range(inicio, fim+1, passos):
    print(i)
