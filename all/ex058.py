# ex058: Crie uma função que retorne todos os livros que uma pessoa leu. Cadastre pessoas
def livros(nome, *livros):
    return f"{nome} leu {", ".join(livros)}"

if __name__ == "__main__":
    print(livros("Maria", 'O poder dos Hábitos', 'Hábitos Atómicos'))  # Maria leu O poder dos Hábitos, Hábitos Atómicos
    print(livros("Pedro", 'Como fazer amigos e influenciar pessoas', 'As 48 leis do poder', 'A coragem de ser imperfeito'))  # Pedro leu Como fazer amigos e influenciar pessoas, As 48 leis do poder, A coragem de ser imperfeito
    print(livros("Lucas", 'Os segredos da mente milionária', 'Comece pelo porquê'))  # Lucas leu Os segredos da mente milionária, Comece pelo porquê
