# ex063: Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.

maior = menor = 0
for i in range(8):
    preco = float(input(f'Digite o preço do produto {i+1}: '))

    if i == 0:
        maior = menor = preco
    else:
        if preco > maior:
            maior = preco
        elif preco < menor:
            menor = preco
print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')


""" # Outras maneiras de fazer o mesmo programa
Gostaria de colocar aqui outras maneiras de se fazer este mesmo
programa em especifico, porque ele pode ser escrito de diversas
formas até melhores que esta."""

# Maneira 1
# precos = []

# for i in range(8):
#     preco = float(input(f'Digite o preço do produto {i+1}: '))
#     precos.append(preco)

# maior = max(precos)
# menor = min(precos)

# print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')




# Maneira 2
# maior = menor = 0
# contador = 1

# while contador <= 8:
#     preco = float(input(f'Digite o preço do produto {contador}: '))
    
#     if contador == 1:
#         maior = menor = preco
#     else:
#         maior = max(maior, preco)
#         menor = min(menor, preco)
    
#     contador += 1

# print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')

# print("\n" + "="*50 + "\n")
