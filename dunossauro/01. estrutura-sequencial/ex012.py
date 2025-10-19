# ex012: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:
# Formula
# Gigabytes * 1024
gigabytes = int(input("Digite a quantidade de Gigabytes do arquivo: "))
megabytes = gigabytes * 1024

print(f"A conversão de {gigabytes} Gigabytes para Megabytes é {megabytes}.")
