# ex210: Efetue cálculo e apresente o valor de uma prestação de um bem em atraso, utilizando a forma PRESTAÇÃO = VALOR + (VALOR * (TAXA / 100) * TEMPO)
valor = float(input("Digite o valor do bem em atraso: "))
taxa = float(input("Digite a taxa de juros: "))
tempo = int(input("Digite o tempo em dias: "))

prestacao = valor + (valor * (taxa / 100) * tempo)

print(f"O valor da prestação é de R${prestacao}.")
