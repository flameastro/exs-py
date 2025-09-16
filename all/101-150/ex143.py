# ex143: Crie uma classe Aluno com atributos nome e notas, e um método para calcular a média.
class Aluno:
    def __init__(self, nome: str, notas: list):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)

        print(f"{media:.2f}")


if __name__ == "__main__":
    aluno1 = Aluno("Pedro", [7.2, 9.5, 2.3])
    aluno1.calcular_media()  # 6.33

    aluno2 = Aluno("Maria", [4.6, 9.3, 4.7])
    aluno2.calcular_media()  # 6.20

    aluno3 = Aluno("Mateus", [7,.3, 9.0, 4.1])
    aluno3.calcular_media()  # 5.10

