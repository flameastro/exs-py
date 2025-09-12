# ex097: Crie um programa que receba o nome de um arquivo como parâmetro e retorne o conteúdo do arquivo
def retorna_conteudo_arquivo(arquivo: str):
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            f.seek(0)
            conteudo = f.read()

            return f"Conteúdo:\n---------------------------------------\n{conteudo}\n---------------------------------------"
    except FileNotFoundError as file_found_e:
        return f"Arquivo não encontrado: {file_found_e}"
    except OSError as os_e:
        return f"Erro de sistema: {os_e}"
    except SyntaxError as syntax_e:
        return f"Erro de sintaxe: {syntax_e}"
    except NameError as name_e:
        return f"Erro de nome: {name_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_conteudo_arquivo("arquivo.txt"))  # [conteúdo]
    print(retorna_conteudo_arquivo("README.md"))  # Arquivo não encontrado: [Errno 2] No such file or directory: 'README.md'
    print(retorna_conteudo_arquivo(7))  # Erro de sistema: [WinError 6] Identificador inválido
