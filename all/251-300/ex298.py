# ex298: As maçãs custam R$ 1.50 cada se forem compradas menos de uma dúzia, e R$ 1.30 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
macas = int(input("Digite o total de maçãs que foram compradas: "))

if macas < 12:
    preco = 1.50
else:
    preco = 1.30

total = preco * macas

print(f"O total é R${total}")
