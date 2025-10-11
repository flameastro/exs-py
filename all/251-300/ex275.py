# ex275: Escreva um programa que copie o conteúdo de um arquivo para um novo arquivo. Seu programa deve verificar se o primeiro arquivo realmente existe.
try:
    arquivo_leitura = input("Qual o arquivo deseja ler? ")

    with open(arquivo_leitura, "r", encoding="utf-8") as f:
        f.seek(0)
        conteudo = f.read()
except Exception as e:
    print(f"Ocorreu um erro ao tentar abrir o arquivo de leitura. Verifique novamente. Erro: {e}")

try:
    arquivo_destino = input("Qual será o arquivo de destino? ")

    if arquivo_destino == arquivo_leitura:
        print("Você não pode copiar e colar o conteúdo no mesmo arquivo.")
    else:
        with open(arquivo_destino, "w", encoding="utf-8") as f:
            f.write(conteudo)
except Exception as e:
    print(f"Ocorreu um erro ao tentar criar o arquivo de destino. Verifique novamente. Erro: {e}")

