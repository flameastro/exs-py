# ex212: Construir um programa que calcule e apresente em metros por segundo o valor da velocidade de um projétil que percorre uma distância em quilômetros a um espaço de tempo em minutos. Utilize a fórmula VELOCIDADE = (DISTÂNCIA * 1000) / (TEMPO * 60)
distancia = float(input("Digite a distância em quilômetros: "))
tempo = int(input("Digite o tempo em minutos: "))

velocidade = (distancia * 1000) / (tempo * 60)
print(f"A velocidade do projétil é de {velocidade} m/s.")
