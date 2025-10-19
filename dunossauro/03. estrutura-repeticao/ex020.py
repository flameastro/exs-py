# ex020: Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
quantidade = int(input("Quantas vezes deseja calcular o fatorial de algum número? "))
while quantidade not in range(0, 11):
    print("O valor da quantidade é muito alto. Tente um valor entre 0 a 10.")
    quantidade = int(input("Quantas vezes deseja calcular o fatorial de algum número? "))

for _ in range(quantidade):
    numero = int(input("Insira o número que deseja descobrir o fatorial: "))
    while numero not in range(1, 17):
        print("Por favor, certifique-se de inserir um valor válido.")
        numero = int(input("Insira o número que deseja descobrir o fatorial: "))

    fatorial = 1

    for i in range(1, numero+1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial} ({"x".join([str(x) for x in range(numero, 0, -1)])} = {fatorial})")

