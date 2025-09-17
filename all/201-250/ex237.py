# ex237: Desconto Simples: Peça o valor de um produto e aplique um desconto de 10%, imprimindo o valor final.
valor = float(input("Digite o valor do produto: "))
resultado = valor - (valor * 10) / 100

print(f"O preço do produto com 10% de desconto é R${resultado}")
