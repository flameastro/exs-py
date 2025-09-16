# ex111: Um grupo de amigos decidiu criar uma sociedade secrta. O nome dessa sociedade será a primeira letra de cada nome do grupo de amigos. Crie uma função que receba uma lista de nomes e retorne o nome da sociedade secreta.
def nome_sociedade_secreta(membros: list):
    nome = ""

    if len(membros) < 2:
        return "A lista deve possuir ao menos dois membros."

    for membro in membros:
        primeira_letra = membro[0]
        nome += primeira_letra

    return f"Nome da sociedade: {nome}"


if __name__ == "__main__":
    print(nome_sociedade_secreta(["João", "Maria", "Pedro", "Ana"]))  # Nome da sociedade: JMPA
    print(nome_sociedade_secreta(["Pedro", "Gabriel", "Gustavo", "Renata", "Marcos", "José"]))  # Nome da sociedade: PGGRMJ
    print(nome_sociedade_secreta(["Marcos"]))  # A lista deve possuir ao menos dois membros.
    print(nome_sociedade_secreta(["Marcos", "Felipe"]))  # Nome da sociedade: MF
