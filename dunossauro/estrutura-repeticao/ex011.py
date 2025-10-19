# ex011: Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))

soma = 0
if n1 > n2:
    for numero in range(n1, n2-1, -1):
        print(numero)
        soma += numero
else:
    for numero in range(n1, n2+1):
        print(numero)
        soma += numero

print(f"A soma dos números é: {soma}")
