# ex077: Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

idades = []
maior18 = menor5 = 0
for i in range(10):
    idade = int(input(f'Digite a idade da pessoa {i+1}: '))
    while idade < 0 or idade > 120:
        idade = int(input(f'Digite a idade corretamente {i+1}: '))
        
    idades.append(idade)

    if idade > 18:
        maior18 += 1

    if idade < 5:
        menor5 += 1

media = sum(idades) / len(idades)
maior = max(idades)

print(f'A média das idades é de {media}')
print(f'Há {maior18} pessoas maiores de 18 anos')
print(f'Há {menor5} pessoas menores de 5 anos')
print(f'A maior idade foi {maior}')
