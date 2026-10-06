# ex352: Faça um programa em que leia uma sequência de 10 letras (caracteres de A a Z), as armazene em um vetor de 10 posições e imprima a lista de letras repetidas no vetor.
# Sendo assim, para os dados:
# `A J G A D F G A A B`
# a saída deve ser:
# `A G.` 
letras = []
repetidas = []

for i in range(10):
    valor = input(f"{i}: ")
    letras.append(valor)

    if letras.count(valor) > 1 and valor not in repetidas:
        repetidas.append(valor)

print(repetidas)
