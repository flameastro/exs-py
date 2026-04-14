# ex319: Escreva um algoritmo que leia uma quantidade qualquer de números, fornecidos pelo usuário. Faça a contagem e exiba quantos estão nos seguintes intervalos: [0 a 25.9], [26 a 50.9], [51 a 75.9] e [76 a 100], sendo que a entrada de dados deve terminar quando for digitado um número negativo.
intervalos = [0] * 4

while True:
    numero = int(input("Insira um número: "))

    if numero < 0:
        print("Foi digitado um número negativo, encerrando a execução do programa")
        break

    if numero >= 0 and numero < 25.9:
        intervalos[0] += 1
    elif numero >= 26 and numero < 50.9:
        intervalos[1] += 1
    elif numero >= 51 and numero < 75.9:
        intervalos[2] += 1
    elif numero >= 76 and numero <= 100:
        intervalos[3] += 1

print(f"Foram fornecidos {intervalos[0]} números num intervalo entre 0 a 25.9")
print(f"Foram fornecidos {intervalos[1]} números num intervalo entre 26 a 50.9")
print(f"Foram fornecidos {intervalos[2]} números num intervalo entre 51 a 75.9")
print(f"Foram fornecidos {intervalos[3]} números num intervalo entre 76 a 100")
