# ex267: Crie uma classe `Filme` com atributos `titulo`, `diretor`, `ano` e métodos de assistir, comprar alimento ou recurso e avaliar o filme.
class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def assistir_filme(self):
        return f"Você está assistindo {self.titulo}"

    def comprar_recurso(self, alimento):
        return f"Você comprou {alimento}. Pronto para assistir?"

    def avaliar_filme(self, nota):
        if (isinstance(nota, int) or isinstance(nota, float)) and (nota >= 0 or nota <= 10):
            return "Obrigado pela sua avaliação."

        return "Avaliação inválida!"


if __name__ == "__main__":
    toy_story = Filme("Toy Story", "John Lasseter", 1995)
    print(toy_story.comprar_recurso("pipoca"))  # Você comprou pipoca. Pronto para assistir?
    print(toy_story.assistir_filme())  # Você está assistindo Toy Story
    print(toy_story.avaliar_filme(9))  # Obrigado pela sua avaliação.
