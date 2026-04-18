# ex337: O número 3025 possui uma característica interessante, sendo a seguinte: 30 + 25 = 55 e * 55 ^ 2 = 3025 Elaborar um algoritmo que verifique se um número inteiro de quatro algarismos (digitado) tem essa propriedade ou não.
n = str(int(input("Digite um número com 4 dígitos inteiro: ")))
if len(n) == 4:
    resultado = (int(n[:2]) + int(n[2:])) ** 2
    if resultado == int(n):
        print(f"O número {n} tem essa propriedade")
    else:
        print(f"O número {n} não possui essa propriedade")
else:
    print("Por favor, insira um valor inteiro de 4 dígitos.")
