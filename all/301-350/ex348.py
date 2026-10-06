# ex348: Faça um programa que leia duas sequências de n inteiros em dois vetores distintos, digamos, v e w e verifique se os dois vetores são idênticos.
n = 10
v = []
w = []

print("Vetor v")
for i in range(n):
    valor = input("Valor: ")
    v.append(valor)

print("Vetor w")
for i in range(n):
    valor = input("Valor: ")
    w.append(valor)

# Verificando vetores
identicos = True

for i in range(len(v)):
    if v[i] != w[i]:
        identicos = False

if identicos:
    print("São idênticos")
else:
    print("São diferentes")
