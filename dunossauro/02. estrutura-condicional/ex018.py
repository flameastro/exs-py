# ex018: Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def valida_data():
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    if data.count("/") != 2:
        return "❌ Data inválida."

    data = data.split("/")
    for elemento in data:
        if not elemento.isnumeric():
            return "❌ Data inválida."

    if (len(data[0]) != 2 or int(data[0]) < 1 or int(data[0]) > 33) or (len(data[1]) != 2 or int(data[1]) < 1 or int(data[1]) > 12):
        return "❌ Data inválida."

    return "✅ Data válida."


print(valida_data())
