# ex022: Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
numero = int(input("Insira um número inteiro: "))

divisores = [str(divisivel) for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(f"{numero} não é um número primo (número composto)")
    print(f"Seus divisores são: {", ".join(divisores)}")
else:
    print(f"{numero} é um número primo.")
