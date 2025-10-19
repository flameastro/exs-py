# ex010: Faça um programa que pergunte em que turno você estuda. Peça para digitar:
# M - Matutino
# V - Vespertino
# N - Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Selecione o seu turno correspondente.")
print("Digite M para Matutino")
print("Digite V para Vespertino")
print("Digite N para Noturno")

turno = input("Em que turno você estuda/trabalha? ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
