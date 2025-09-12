# ex029: # Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
soma = 0
for i in range(500, 0, -50):
    soma += i

print(f'O resultado da expressão é {soma}')
