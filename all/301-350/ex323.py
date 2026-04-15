# ex323: Codifique um algoritmo Histograma, que exiba um histograma da variação da temperatura durante a semana. Por exemplo, se as temperaturas forem 19°C, 21 °C, 25°C, 22°C, 20°C, 17°C e 15°C, de domingo a sábado, respectiva men te, o algoritmo deverá exibir:
# D: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# S: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# T: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# Q: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# Q: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# S: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# S: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# Suponha que nenhuma temperatura seja maior que 80°C nem menor que -80°C.
def mostra_histograma(letra: str, pos: int) -> None:
    print(f"{letra}: {"■ " * temperaturas[pos]}")

temperaturas = []

for dia in range(7):
    temperatura = int(input(f"Digite a temperatura do dia {dia+1}: "))
    while temperatura > 80 or temperatura < -80:
        print("Por favor, insira um temperatura entre -80 a 80 graus Celsius")
        temperatura = int(input(f"Digite a temperatura do dia {dia+1}: "))

    temperaturas.append(temperatura)

mostra_histograma("D", 0)
mostra_histograma("S", 1)
mostra_histograma("T", 2)
mostra_histograma("Q", 3)
mostra_histograma("Q", 4)
mostra_histograma("S", 5)
mostra_histograma("S", 6)
