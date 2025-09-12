# ex117: # Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.
def mostrar_soma_e_numeros():
    numeros = []
    total = 0

    try:
        for i in range(5):
            numero = int(input(f'Digite o número {i+1}: '))

            numeros.append(numero)
            total += numero
    except ValueError as value_e:
        return f"A lista pode conter apenas números. Erro: {value_e}"
    except Exception as e:
        return f"Erro: {e}"

    return (f'A soma dos números digitados é {total}\n'
            f'Os números digitados foram: {numeros}')


if __name__ == "__main__":
    print(mostrar_soma_e_numeros())
