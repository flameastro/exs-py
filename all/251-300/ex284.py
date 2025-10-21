# ex284: Crie um programa que peça ao usuário em que turno o usuário estuda. Considerando as seguintes opções:
# Matutino -> "Bom Dia!"
# Vespertino -> "Boa Tarde!"
# Noturno -> "Boa Noite!"
# Outro valor -> "Valor Inválido"
turno = input("Digite o turno que você estuda (Matutino, Vespertino ou Noturno): ").capitalize()

print("Bom dia!" if turno == "Matutino" else "Boa Tarde!" if turno == "Vespertino" else "Boa noite!" if turno == "Noturno" else "Valor inválido.")
