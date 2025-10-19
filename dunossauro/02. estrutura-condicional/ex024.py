# ex024: Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(" OPERAÇÕES PERMITIDAS ".center(50, "-"))
print("+ -> Adição")
print("- -> Subtração")
print("* -> Multiplicação")
print("/ -> Divisão")
operacao = input("Qual operação deseja realizar? ").lower()
if operacao == "+":
    numero = n1 + n2
elif operacao == "-":
    numero = n1 - n2
elif operacao == "*":
    numero = n1 * n2
elif operacao == "/":
    numero = n1 / n2
else:
    print("Por favor, insira um valor válido.")
    numero = None

if numero is not None:
    print(f"O resultado do número é {numero}")
    print(" Detalhes sobre o número inserido ".center(50, "-"))
    print("PAR" if numero % 2 == 0 else "ÍMPAR")
    print("POSITIVO" if numero > 0 else "NEGATIVO")
    print("INTEIRO" if numero.is_integer() else "DECIMAL")
