# ex007: Faça um programa que use a função valor_pagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valor_pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução, o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento, o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def valor_pagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    else:
        return valor * (1 + 0.03 + 0.001 * dias_atraso)

total_prestacoes = 0
quantidade_prestacoes = 0

while True:
    valor = float(input("Digite o valor da prestação (0 para sair): "))

    if valor == 0:
        break

    dias = int(input("Digite o número de dias em atraso: "))

    valor_pago = valor_pagamento(valor, dias)

    print(f"Valor a ser pago: R$ {valor_pago:.2f}\n")

    total_prestacoes += valor_pago
    quantidade_prestacoes += 1

print("\n=== Relatório do dia ===")
print(f"Quantidade de prestações pagas: {quantidade_prestacoes}")
print(f"Valor total de prestações pagas: R$ {total_prestacoes:.2f}")
