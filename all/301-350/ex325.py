# ex325: Elabore um algoritmo que crie dois vetores A e B de 10 elementos e, a partir deles, crie um vetor C, composto pela união dos elementos de A e B. dispostos em ordem crescente, exibindo o resultado.
vetor_a = []
vetor_b = []
vetor_c = []

# Pede ao usuário preencher os vetores
for elemento in range(10):
    vetor_a.append(int(input(f"Insira um valor para o vetor A, posição {elemento}: ")))
    vetor_b.append(int(input(f"Insira um valor para o vetor B, posição {elemento}: ")))


for elemento in range(10):
    # Adiciona os elementos do vetor a e do vetor b caso o elemento atual não tenha no vetor C
    if vetor_a[elemento] not in vetor_c:
        vetor_c.append(vetor_a[elemento])

    if vetor_b[elemento] not in vetor_c:
        vetor_c.append(vetor_b[elemento])

vetor_c.sort()  # Ordena os elementos do vetor C em ordem crescente
print(f"A união dos elementos de A e B são {vetor_c}")
