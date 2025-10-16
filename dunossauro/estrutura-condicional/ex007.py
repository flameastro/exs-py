# ex007: Faça um programa que leia três números e mostre o maior e o menor deles:
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

if n1 < n2 and n1 < n3:
    print(f"O menor número é o primeiro -> {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor número é o segundo -> {n2}")
elif n3 < n1 and n3 < n2:
    print(f"O menor número é o terceiro -> {n3}")
else:
    if n1 == n2 and n1 == n3:
        print(f"Todos são iguais -> {n1}")
    elif n1 == n2:
        print(f"Ambos o primeiro e o segundo número são iguais -> {n1}")
    elif n2 == n3:
        print(f"Ambos o segundo e o terceiro número são iguais -> {n2}")
    elif n1 == n3:
        print(f"Ambos o primeiro e o terceiro número são iguais -> {n1}")
