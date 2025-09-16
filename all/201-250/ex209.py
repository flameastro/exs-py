# ex209: Efetue o cálculo da quantidade de litros de combustível gastos durante uma viagem. Considere: distancia = tempo * velocidade. litros = distancia / 12
tempo = int(input("Digite o tempo da viagem em horas: "))
velocidade = int(input("Digite a velocidade da viagem em km/h: "))

distancia = tempo * velocidade
litros = distancia / 12

print(f"Distância percorrida: {distancia}")
print(f"O total de litros gastos foram {litros}.")
