# ex146: Crie uma classe Livro com atributos título e autor, e um método para exibir informações.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacoes(self):
        print(f"O autor {self.autor} escreveu o livro {self.titulo}")


if __name__ == "__main__":
    livro = Livro("Técnicas de Invasão", "Bruno Fraga")
    livro.exibir_informacoes()  # O autor Bruno Fraga escreveu o livro Técnicas de Invasão
