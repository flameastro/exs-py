# ex011: Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mes_por_extenso de AAAA. Opcionalmente, valide a data e retorne None caso a data seja inválida.
def formata_data(data):
    if data.count("/") != 2:
        return "❌ Data inválida."

    data = data.split("/")
    for elemento in data:
        if not elemento.isnumeric():
            return "❌ Data inválida."

    if (len(data[0]) != 2 or int(data[0]) < 1 or int(data[0]) > 33) or (len(data[1]) != 2 or int(data[1]) < 1 or int(data[1]) > 12):
        return "❌ Data inválida."

    dia = data[0]
    mes = data[1]
    ano = data[2]
    MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    return f"{dia} de {MESES[int(mes)-1]} de {ano}"


if __name__ == "__main__":
    print(formata_data("12/05/2005"))  # 12 de Maio de 2005
    print(formata_data("15/25/2003"))  # ❌ Data inválida.
    print(formata_data("29/12/540"))  # 29 de Dezembro de 540
