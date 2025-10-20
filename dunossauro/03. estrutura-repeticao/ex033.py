# ex033: O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
print(" Instruções ".center(50, "-"))
print("Digite uma temperatura em graus celsius")
print("Digite -0.1 para sair")
print("".center(50, "-"))
temperaturas = []
contador = 1

while True:
    temperatura = float(input(f"Insira a temperatura {contador}: "))

    if temperatura == -0.1:
        break

    temperaturas.append(temperatura)
    contador += 1

menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print(f"A menor temperatura registrada foi {menor:.2f} graus celsius.")
print(f"A maior temperatura registrada foi {maior:.2f} graus celsius.")
print(f"A média das temperaturas registradas é de {media:.2f} graus celsius.")
