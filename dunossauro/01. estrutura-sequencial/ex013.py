# ex013: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

# Para Megabytes: Gigabytes * 1024
# Para Kilobytes: Gigabytes * 1024 * 1024
# Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
gigabytes = int(input("Digite a quantidade de Gigabytes do arquivo: "))
megabytes = gigabytes * 1024
kilobytes = gigabytes * 1024 * 1024

print(f"{gigabytes} Gigabytes equivalem a {megabytes} megabytes ou {kilobytes} kilobytes.")
