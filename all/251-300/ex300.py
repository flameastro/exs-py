# ex300: O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor
custo_fabrica = float(input("Qual o custo de fábrica? R$"))
PORCENTAGEM_DISTRIBUIDOR = 0.28
IMPOSTOS = 0.45

custo_carro = (custo_fabrica + (custo_fabrica * IMPOSTOS)) + (custo_fabrica * PORCENTAGEM_DISTRIBUIDOR)
print(f"O custo do carro final é de R${custo_carro}")
