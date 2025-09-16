# ex219: Efetuar a leitura de um valor numérico inteiro que esteja na faixa de valores de 1 até 9. O programa deve apresentar a mensagem "O valor está na faixa permitida", caso o valor informado esteja entre 1 e 9. Se o valor estiver fora da faixa, o programa deve apresentar a mensagem "O valor está fora da faixa permitida".
n = int(input("Digite um valor numérico inteiro: "))

if n >= 1 and n <= 9:
    print("O valor está na faixa permitida")
else:
    print("O valor está fora da faixa permitida")
