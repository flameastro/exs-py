# ex218: Ler cinco valores numéricos inteiros (variáveis A, B, C, D e E), identificar e apresentar o maior e o menor valores informados
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
E = int(input("Digite o valor de E: "))

valores = sorted([A, B, C, D, E])

print(f"O menor valor é {valores[0]}.")
print(f"O maior valor é {valores[-1]}.")
