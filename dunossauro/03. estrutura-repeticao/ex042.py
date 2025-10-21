# ex042: Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
numeros = []
while True:
    numero = int(input("Insira um número: "))
    while numero > 100:
        print("Por favor, insira um número menor que 100.")
        numero = int(input("Insira um número: "))

    if numero <= 0:
        break

    numeros.append(numero)

media = sum(numeros) / len(numeros)
print(f"Média: {media:.2f}")

if media >= 0 and media <= 25:
    print("Os números informados estão no intervalo de 0 a 25.")
elif media >= 26 and media <= 50:
    print("Os números informados estão no intervalo de 26 a 50.")
elif media >= 51 and media <= 75:
    print("Os números informados estão no intervalo de 51 a 75.")
elif media >= 76 and media <= 100:
    print("Os números informados estão no intervalo de 76 a 100.")
