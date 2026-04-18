# ex333: Descreva como descobrir a moeda falsa em um grupo de cinco moedas, fazendo uso de uma balança analítica (sabe-se que a moeda falsa é mais leve que as outras), com o menor número de pesagens possível. Lembre-se de que sua descrição deve resolver o problema para qualquer situação.
# Dica: É possível resolver com apenas duas pesagens.
grupoA = [1, 1]
grupoB = [1, 1]
moeda_restante = 0.5

if sum(grupoA) > sum(grupoB):
    if grupoB[0] == grupoB[1]:
        print(f"A moeda falsa é a moeda restante")
    elif grupoB[0] > grupoB[1]:
        print(f"A moeda falsa está na segunda posição do grupo B")
    else:
        print(f"A moeda falsa está na primeira posição do grupo B")
elif sum(grupoB) > sum(grupoA):
    if grupoA[0] == grupoB[1]:
        print("A moeda falsa é a moeda restante")
    elif grupoA[0] > grupoA[1]:
        print("A moeda falsa está na segunda posição do grupo A")
    else:
        print(f"A moeda falsa está na primeira posição do grupo A")
elif sum(grupoA) == sum(grupoB):
    print("A moeda falsa é a moeda restante")
