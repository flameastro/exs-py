# ex324: Faça um algoritmo que construa dois vetores A e B de 10 elementos e, a partir deles, crie um vetor C, composto pela soma dos elementos, sendo: C[0] = A[0] + B[9], C[1] = A[1] + B[8], C[2] = A[2] + B[7] etc.
from random import randint as random

vetor_A = []
vetor_B = []
vetor_C = []

# Construção dos dois vetores A e B -> Preenche com valores aleatórios
for _ in range(10):
    vetor_A.append(random(1, 100))
    vetor_B.append(random(1, 100))

# Percorre cada elemento de ambos os vetores A e B e soma
for elemento in range(10):
    soma = vetor_A[elemento] + vetor_B[- (elemento + 1)]
    vetor_C.append(soma)

print(f"A soma dos vetores A e B são {vetor_C}")
