# ex013: Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

if expoente == 0:
    print(1)
else:
    resultado = base
    for i in range(1, abs(expoente)):
        resultado *= base

    if expoente < 0:
        print(f"O resultado da exponenciação é {1 / resultado}")
    else:
        print(f"O resultado da exponenciação é {resultado}")
