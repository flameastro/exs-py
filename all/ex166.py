# ex166: Crie uma função que converta nomes em inicias separados por pontos. Exemplo: Albert Einstein -> A.E
def acronimo_nome(nome: str):
    iniciais = []

    for inicial in nome.split():
        iniciais.append(inicial[0])

    return ".".join(iniciais)


if __name__ == "__main__":
    print(acronimo_nome("Albert Einstein"))  # A.E
    print(acronimo_nome("Isaac Newton"))  # I.N
    print(acronimo_nome("Leonardo Da Vinci"))  # L.D.V
