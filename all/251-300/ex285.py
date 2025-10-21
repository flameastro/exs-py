# ex285: Num cinema, após o filme, cada espectador respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
# Excelente -> 3;
# Bom -> 2;
# Regular -> 1
# Crie um algoritmo que peça a idade e a opnião de 10 espectadores, e imprima:
# A média das idades das pessoas que responderam Excelente;
# A quantidade de pessoas que responderam regular;
# A porcentagem de pessoas que responderam bom entre todos os expectadores analisados.
excelente = []
regular = []
bom = []

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    while idade not in range(0, 121):
        print("Por favor, digite um valor correto.")
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))

    opniao = int(input(f"Digite a opnião da pessoa {i+1} (Excelente -> 3; Bom -> 2; Regular -> 1): "))
    while opniao not in range(1, 4):
        print("Por favor, digite um valor entre 1 a 3, de acordo com a classificação:\nExcelente -> 3\nBom -> 2\nRegular -> 1")
        opniao = int(input(f"Digite a opnião da pessoa {i+1}: "))

    if opniao == 3:
        excelente.append(idade)
    elif opniao == 2:
        regular.append(idade)
    else:
        bom.append(idade)

tamanho_excelente = 0
soma_excelente = 0
for idade in excelente:
    soma_excelente += idade
    tamanho_excelente += 1

media_excelente = soma_excelente / tamanho_excelente

quantidade_regular = 0
for idade in regular:
    quantidade_regular += 1


quantidade_bom = 0
for idade in bom:
    quantidade_bom += 1

porcentagem_bom = (quantidade_bom / 10) * 100

print(f"A média das idades das pessoas que responderam excelente é {media_excelente}")
print(f"A quantidade de pessoas que responderam regular é {quantidade_regular}")
print(f"A porcentagem de pessoas que responderam bom é {porcentagem_bom}%")
