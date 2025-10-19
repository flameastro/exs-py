# ex014: João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso = float(input("Digite o peso total dos peixes em kg: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

    print(f"O excesso de quilos de peixe é {excesso}, e a multa é de R${multa}.")
else:
    print("Não houve excesso de peso.")
