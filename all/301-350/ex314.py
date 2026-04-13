# ex314: # As lojas de um shopping center estão concedendo 10% de desconto no preço de qualquer produto. Faça um algoritmo que, a partir do valor fornecido, calcule e exiba o preço atual e o preço com o desconto.
preco = float(input("Digite o valor do preço do produto: R$"))
porcentagem_desconto = 10

preco_com_desconto = preco - (preco * (porcentagem_desconto / 100))
print(f"O novo preço com desconto é de R${preco_com_desconto}")
