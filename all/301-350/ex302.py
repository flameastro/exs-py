# ex302: Crie uma classe Album, que representa um Album de Músicas. Adicione atributos titulo, artista, ano, genero, musicas. Com os métodos adicionar_musica, remover_musica, listar_musicas, escutar_musica.
class Album:
    def __init__(self, titulo: str, ano: int = None, musicas: list = [], genero: str = None, artista: str = None):
        self.titulo = titulo
        self.artista = artista
        self.ano = ano
        self.genero = genero
        self.musicas = musicas

    def adicionar_musica(self, musica: str) -> str:
        try:
            self.musicas.append(musica.title())
            return f"Música adicionada com sucesso na lista de músicas."
        except Exception as e:
            return f"Erro, verifique se você inseriu uma música adequada. Erro: {e}"

    def remover_musica(self, musica: str) -> str:
        try:
            if musica.title() not in self.musicas:
                return "A música não está presente na lista."

            self.musicas.remove(musica.title())
            return "Música removida com sucesso."
        except Exception as e:
            return f"Erro, verifique se você inseriu uma música adequada. Erro: {e}"

    def listar_musicas(self) -> str:
        try:
            if len(self.musicas):
                return f"Lista de músicas: \n{"\n".join([musica for musica in self.musicas])}"

            return "Ops, não há nenhuma música na lista."
        except Exception as e:
            return f"Algum erro inesperado ocorreu. Erro: {e}"

    def escutar_musica(self, musica: str) -> str:
        try:
            if musica.title() not in self.musicas:
                return "Essa música não está no Album."

            return f"Escutando \"{musica.title()}\""
        except Exception as e:
            return f"Algum erro inesperado ocorreu. Erro: {e}"


if __name__ == "__main__":
    mgmt = Album("MGMT")
    print(mgmt.adicionar_musica("Inside The Body"))  # Música adicionada com sucesso na lista de músicas.
    print(mgmt.listar_musicas())  # Lista de músicas:    Inside The Body
    print(mgmt.remover_musica("inside the body"))  # Música removida com sucesso.
    print(mgmt.listar_musicas())  # Lista de músicas:    
    print(mgmt.adicionar_musica("Little Dark Age"))  # Música adicionada com sucesso na lista de músicas.
    print(mgmt.escutar_musica("little dark age"))  # Escutando "Little Dark Age"
