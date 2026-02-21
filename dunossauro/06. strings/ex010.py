# ex010: Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
def numero_por_extenso(numero):
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dez_a_dezenove = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return dez_a_dezenove[numero - 10]
    else:
        dezena = numero // 10
        unidade = numero % 10

        if unidade == 0:
            return dezenas[dezena]
        else:
            return f"{dezenas[dezena]} e {unidades[unidade]}"


numero = int(input("Digite um número entre 0 e 99: "))

if 0 <= numero <= 99:
    print(f"{numero} por extenso é: {numero_por_extenso(numero)}")
else:
    print("Número fora do intervalo permitido (0 a 99).")
