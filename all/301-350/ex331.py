# ex331: Dadas as temperaturas que foram registradas, diariamente, durante uma semana, deseja-se determinar em quantos dias desta semana a temperatura esteve acima da média.
# A solução para este problema envolve os seguintes passos:
# a) Obter os valores das temperaturas.
# b) Calcular a média desses valores.
# c) Verificar quantos deles são maiores que a média.

# Variáveis
maiores_media = []
temperaturas = []
soma = 0

for dia in range(7):
    # Pede ao usuário a temperatura de cada dia, guarda na variável temperaturas e soma a temperatura
    temperatura = round(float(input(f"Digite a temperatura em Celsius do dia {dia+1}: ")), 2)
    temperaturas.append(temperatura)
    soma += temperatura

media = round(soma / 7, 2)  # Calcula a média
print(f"A média das temperaturas foi: {media}")

# Para cada dia e temperatura na lista de temperaturas, adiciona o dia e a temperatura na lista maiores_media se a temperatura daquele dia for maior que a media
for dia, temperatura in enumerate(temperaturas):
    if temperatura > media:
        maiores_media.append([dia+1, temperatura])

# Apresenta os resultados
print(f"{len(maiores_media)} dias foram maiores que a média.\nSão eles:")
print(f"{"Dia":<10} Temperatura")
for dia, temperatura in maiores_media:
    print(f"{dia:<10} {temperatura}")
