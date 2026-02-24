# ex305: Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escreva um programa, que imprima o tempo em anos necessário para que a população do país A ultrapasse a população do país B.
pais_a = 5000000
taxa_a = 0.03
pais_b = 7000000
taxa_b = 0.02

anos = 0

while pais_a < pais_b:
    pais_a = pais_a + (pais_a * taxa_a)
    pais_b = pais_b + (pais_b * taxa_b)
    anos += 1


print(f"Quantidade de anos: {anos}")
