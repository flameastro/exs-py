# ex104: Conte quantas linhas tem um arquivo.

def conta_linhas_arquivo(arquivo: str):
    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo:
            arquivo.seek(0)

            linhas = 0
            for _ in arquivo.readlines():
                linhas += 1
            arquivo.seek(0)

            return f"Quantidade de linhas encontradas: {linhas}"
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado/não existe. Verifique o caminho do arquivo ou crie um."
    except Exception as erro:
        return f"Erro: {erro}"


print(conta_linhas_arquivo("arquivo.txt"))
