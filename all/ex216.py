# ex216: Ler três valores inteiros representados pelas variáveis A, B e C e apresentar os valores lidos dispostos em ordem crescente.
A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))
C = int(input('Digite o terceiro número: '))

lista = [str(A), str(B), str(C)]

print(f'Os números em ordem crescente são {", ".join(sorted(lista))}')
