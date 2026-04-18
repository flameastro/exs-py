# ex341: Um número inteiro é considerado triangular se este for o produto de três números inteiros consecutivos, como, por exemplo 120 = 4 * 5 * 6 Elabore um algoritmo que, após ler um número n, verifique se o mesmo é ou não triangular.
n = int(input("Insira um número inteiro e positivo: "))
triangular = False

for x in range(1, (n // 2)+1):
    n2 = x + 1
    n3 = x + 2
    produto = x * (n2) * (n3)

    if produto == n:
        print(f"O número é triangular e os números consecutivos são: {x} x {n2} x {n3} = {n}")
        triangular = True

if not triangular:
    print(f"O número {n} não é triangular")
