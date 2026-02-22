# ex303: Escreva um algoritmo para ler 2 números e escrever a soma dos inteiros existentes entre os 2 números lidos (incluindo os números lidos na soma). Exemplo: Números lidos: 2 e 5 Resultado: 2+3+4+5 = 14. Observação: Considere que o segundo valor lido será sempre maior que o primeiro valor lido.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 < numero2:
    soma = 0

    for x in range(numero1, numero2+1):
        soma += x

    print(f"Resultado: {soma}")
else:
    print("O segundo número deve ser maior que o primeiro")
