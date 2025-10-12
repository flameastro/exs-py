# ex276: Crie uma classe YouTube que tem como herança Canal e Video
class YouTube:
    def __init__(self):
        self.versao = 1.0
        self.tema = "Escuro"


class Canal(YouTube):
    def __init__(self, nome_usuario, nome_canal, descricao, inscritos, quantidade_videos, total_visualizacoes, data_criacao):
        super().__init__()
        self.nome_usuario = nome_usuario
        self.nome_canal = nome_canal
        self.descricao = descricao
        self.inscritos = inscritos
        self.quantidade_videos = quantidade_videos
        self.total_visualizacoes = total_visualizacoes
        self.data_criacao = data_criacao


    def apresentacao(self):
        print(f"""Informações sobre o canal
Nome de usuário: {self.nome_usuario}
Nome do canal: {self.nome_canal}
Descrição: {self.descricao}
Inscritos: {self.inscritos}
Quantidade de vídeos: {self.quantidade_videos}
Total de visualizações: {self.total_visualizacoes}
Data de criação do canal: {self.data_criacao}""")


    def inscrever_se(self, nome_usuario):
        self.inscritos += 1

        if nome_usuario == self.nome_usuario:
            print("Você não pode se inscrever no seu próprio canal")
        print(f"Agora {self.nome_canal} tem {self.inscritos} inscritos")


class Video(YouTube):
    def __init__(self, canal: str, titulo: str, descricao: str, duracao: str, visualizacoes: int = 0, likes: int = 0, deslikes: int = 0, qualidade: int = 1080):
        super().__init__()
        self.canal = canal
        self.titulo = titulo
        self.descricao = descricao
        self.duracao = duracao
        self.visualizacoes = visualizacoes
        self.likes = likes
        self.deslikes = deslikes

        self.usuarios = []
        self.interacoes_like = []
        self.interacoes_deslike = []


    def detalhes(self):
        print(f"""Informações sobre o vídeo
Canal responsável: {self.canal}
Título: {self.titulo}
Descrição: {self.descricao}
Duração: {self.duracao}
Visualizações: {self.visualizacoes}
Quantidade de Likes: {self.likes}
Quantidade de Deslikes: {self.deslikes}""")


    def assistir(self, usuario):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
            self.visualizacoes += 1
            print(f"{usuario} está assistindo o vídeo")
        else:
            print("Assistindo novamente o vídeo")


    def dar_like(self, usuario):
        if usuario not in self.usuarios:
            print("Você deve primeiro assistir ao vídeo")
        elif usuario in self.interacoes_like:
            print("Você já deu um like!")
        else:
            self.interacoes_like.append(usuario)
            self.likes += 1

            print(f"{usuario} deu um like. O vídeo possui {self.likes} likes.")


    def dar_deslike(self, usuario):
        if usuario not in self.usuarios:
            print("Você deve primeiro assistir ao vídeo")
        elif usuario in self.interacoes_deslike:
            print("Você já deu um like!")
        else:
            self.interacoes_deslike.append(usuario)
            self.deslikes += 1

            print(f"{usuario} deu um deslike. O vídeo possui {self.deslikes} deslikes.")


    def comentar(self, usuario, comentario):
        if usuario not in self.usuarios:
            print(f"Para comentar, você precisa assistir o vídeo primeiramente.")
        else:
            print(f"{usuario} comentou: {comentario}")


if __name__ == "__main__":
    curso_em_video = Canal("cursoemvideo", "Curso em Vídeo", "Paixão por Ensinar", 2595900, 1745, 295450230, "10/05/2013")
    video001 = Video(curso_em_video, "Curso de Python - Aula 1", "Olá, Pequeno gafanhoto! Que tal começar a sua jornada de programação em Python?", "23:45", 8094730, 1567500, 0)

    video001.assistir("pedro43889")  # pedro43889 está assistindo o vídeo
    video001.dar_like("mariazinha1")  # Você deve primeiro assistir ao vídeo
    video001.dar_like("pedro43889")  # pedro43889 deu um like. O vídeo possui 1567501 likes.
    video001.assistir("mariazinha1")  # Assistindo o vídeo
    video001.dar_like("mariazinha1")  # mariazinha1 deu um like. O vídeo possui 1567502 likes.
    video001.dar_like("mariazinha1")  # mariazinha1 está assistindo o vídeo
    video001.comentar("pedro43889", "Oi mestre Guanabara, obrigado pelo vídeo! Gostei muito!! Quando vai lançar o próximo vídeo??")  # pedro43889 comentou: Oi mestre Guanabara, obrigado pelo vídeo! Gostei muito!! Quando vai lançar o próximo vídeo??
    video001.assistir("cursoemvideo")  # cursoemvideo está assistindo o vídeo
    video001.comentar("cursoemvideo", "Olá, gafanhoto pedro43889! O próximo vídeo será lançado amanhã e veremos sobre a história do Python! Te espero lá, gafanhoto!")  # cursoemvideo comentou: Olá, gafanhoto pedro43889! O próximo vídeo será lançado amanhã e veremos sobre a história do Python! Te espero lá, gafanhoto!


    manual_do_mundo = Canal("manualdomundo", "Manual do Mundo", "Explore um canal cheio de curiosidades! Adoramos Ciência, Tecnologia, Arquitetura, Mecânica, Física!", 19873500, 3175, 5030000000, "24/07/2006")
    video002 = Video(manual_do_mundo, "Como fazer seu robô com Raspberry PI", "Hoje, vamos ver como se faz um robô, apenas usando Raspberry PI! #borave !!", "14:54", 1350035, 456000, 0, 1080)

    video002.assistir("bernardogamer874")  # bernardogamer874 está assistindo o vídeo
    video002.dar_like("bernardogamer874")  # bernardogamer874 deu um like. O vídeo possui 456001 likes.
    video002.comentar("bernardogamer874", "OI Iberê!! Gostei muito do vídeo! Pode me falar aonde posso encontrar um raspberry pi barato?")  # bernardogamer874 comentou: OI Iberê!! Gostei muito do vídeo! Pode me falar aonde posso encontrar um raspberry pi barato?
    video002.assistir("manualdomundo")  # manualdomundo está assistindo o vídeo
    video002.comentar("manualdomundo", "Fallaaaaa bernardo! Então, você pode encontrar raspberry pi baratos e de ótima qualidade em https://www.raspberrypi.com/products/")  # manualdomundo comentou: Fallaaaaa bernardo! Então, você pode encontrar raspberry pi baratos e de ótima qualidade em https://www.raspberrypi.com/products/
    video002.comentar("bernardogamer874", "Obrigado Iberê!")  # bernardogamer874 comentou: Obrigado Iberê!
    video002.assistir("manualdosubmundoeruim")  # manualdosubmundoeruim está assistindo o vídeo
    video002.comentar("manualdosubmundoeruim", "UUUUU!! Não gostei! Raspberry PI é muito caro!!")  # manualdosubmundoeruim comentou: UUUUU!! Não gostei! Raspberry PI é muito caro!!
    video002.dar_deslike("manualdosubmundoeruim")  # manualdosubmundoeruim deu um like. O vídeo possui 1 deslikes.
