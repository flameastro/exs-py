# ex013: Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
print(" Tabela dos Valores ".center(50, "-"))
DIAS = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]

for i in range(7):
    print(f"{i+1} - {DIAS[i]}")

numero = int(input("Digite um número que corresponde a um dia da semana: "))
while numero not in range(1, 8):
    print("Por favor, certifique-se de escolher um valor válido.")
    numero = int(input("Digite um número que corresponde a um dia da semana: "))

print(f"Você escolheu {DIAS[numero-1]}")
