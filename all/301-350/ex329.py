# ex329: Elaborar um programa que calcule e apresente o resultado do cálculo da fatorial de um número qualquer. Além dessa possibilidade, o programa deve permitir ao usuário fazer novos cálculos até o momento que decidir encerrar o programa.
while True:
    try:
        fatorial = 1
        numero = int(input("Digite um número para o cálculo do fatorial: "))

        for x in range(1, numero+1):
            fatorial *= x

        print(f"O fatorial do número digitado é {fatorial}")
    except ValueError as value_error:
        print(f"Ooops! Parece que você inseriu um valor incorreto. Erro: {value_error}")
    except Exception as error:
        print(f"Um erro aconteceu: {error}")

    continuar = input("Digite \"stop\" para parar ou qualquer outra tecla para continuar: ").lower().strip()
    if continuar == "stop":
        break
