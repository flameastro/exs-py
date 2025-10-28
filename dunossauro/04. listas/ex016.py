# ex016: Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
valor_semana = 200
porcentagem = 0.09
intervalos = [0] * 9

while True:
    venda_bruta = float(input("Venda Bruta (0 para sair): R$"))
    if venda_bruta == 0:
        break

    while venda_bruta < 0 or venda_bruta > 100000:
        print("Por favor, insira um valor válido.")
        venda_bruta = float(input("Venda Bruta: R$"))

    salario = valor_semana + (porcentagem * venda_bruta)

    if salario >= 1000:
        intervalos[8] += 1
    else:
        indice = int((salario - 200) // 100)
        intervalos[indice] += 1

print("\nDistribuição de salários:")
for i in range(8):
    print(f"${200 + i*100} - ${299 + i*100}: {intervalos[i]} vendedores")
print(f"$1000 ou mais: {intervalos[8]} vendedores")
