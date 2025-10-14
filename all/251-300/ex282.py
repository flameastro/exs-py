# ex282: Crie um algoritmo que peça ao usuário uma palavra e imprima essa palavra em escadinhas.
# palavra: AMOR
# A
# AM
# AMO
# AMOR
# ... E em seguida:
# AMOR
# MOR
# OR
# R
palavra = input("Digite uma palavra: ")

for i in range(1, len(palavra)+1):
    print(palavra[:i])

for i in range(0, len(palavra)):
    print(palavra[i:])
