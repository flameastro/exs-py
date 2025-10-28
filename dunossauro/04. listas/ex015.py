# ex015: Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
notas = []
while True:
    nota = float(input("Nota: "))
    if nota == -1:
        break

    while nota < 0 or nota > 10:
        print("Por favor, certifique-se de inserir um valor válido.")
        nota = float(input("Nota: "))

    notas.append(nota)


if len(notas) != 0:
    soma = sum(notas)
    media = soma / len(notas)

    print(f"{'Quantidade de valores lidos':40} {len(notas)}")
    print(f"{'Valores informados':40} {", ".join([str(x) for x in notas])}")
    print(f"{'Valores informados (ordem inversa)':40} {", ".join([str(x) for x in notas[::-1]])}")
    print(f"{'Soma dos valores informados':40} {soma:.2f}")
    print(f"{'Média dos valores informados':40} {media:.2f}")
    print(f"{'Quantidade de valores acima da média':40} {len([x for x in notas if x > media])}")
    print(f"{'Quantidade de valores abaixo de 7':40} {len([x for x in notas if x < 7])}")
    print("-- END! --")
else:
    print("Impossível realizar operações sem nenhum dado.")
