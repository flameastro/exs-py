# ex268: Crie uma aplicação completa com classes `Aluno` e `Professor` e interações entre elas.
class Professor:
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia

    def ensinar(self, aluno, assunto):
        print(f"Na aula de {self.materia}, {self.nome} ensina {aluno.nome} sobre {assunto}")


class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie

    def apresentar(self, professor):
        print(f"OI, {professor.nome}! Meu nome é {self.nome}, tenho {self.idade} anos! Estou na {self.serie}")


if __name__ == "__main__":
    aluno_antonio = Aluno("Antônio", 15, "8a Série")
    professor_rodrigo = Professor("Rodrigo", "Ciências")
    aluno_antonio.apresentar(professor_rodrigo)  # OI, Rodrigo! Meu nome é Antônio, tenho 15 anos! Estou na 8a Série
    professor_rodrigo.ensinar(aluno_antonio, "Moléculas")  # Na aula de Ciências, Rodrigo ensina Antônio sobre Moléculas
