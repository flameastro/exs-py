# ex273: Escreva um programa que converta todas as letras de um arquivo em maiúsculas e escreva o resultado na tela.
arquivo = input("Digite o nome do arquivo: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        f.seek(0)

        for linha in f.readlines():
            print(linha.upper())
except Exception as e:
    print(f"Ocorreu um erro ao tentar abrir o arquivo. Verifique se ele realmente existe. Erro: {e}")
