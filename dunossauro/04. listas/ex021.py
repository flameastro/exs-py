# ex021: Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

# Comparativo de Consumo de Combustível

# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5

# Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.
modelos = []
consumos = []

for i in range(5):
    print(f"Veículo {i + 1}")
    modelo = input("Nome: ").strip()
    consumo = float(input("Km por litro: "))
    modelos.append(modelo)
    consumos.append(consumo)
    print()

print("\nRelatório Final")

DISTANCIA = 1000
PRECO_GASOLINA = 2.25

menor_consumo = None
modelo_mais_economico = ""

for i in range(5):
    litros = DISTANCIA / consumos[i]
    custo = litros * PRECO_GASOLINA
    print(f"{i + 1} - {modelos[i]:15} - {consumos[i]:5.1f} - {litros:7.1f} litros - R$ {custo:6.2f}")

    if menor_consumo is None or litros < menor_consumo:
        menor_consumo = litros
        modelo_mais_economico = modelos[i]

print(f"\nO menor consumo é do {modelo_mais_economico}.")
