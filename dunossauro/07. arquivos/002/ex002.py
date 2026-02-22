# ex002: A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
def analisa_espaco_ocupado(arquivo: str):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            f.seek(0)

            usuarios = []
            armazenamentos = []

            for linha in f.readlines():
                linha = linha.removesuffix("\n").split()

                usuarios.append(linha[0])
                armazenamentos.append(int(linha[1]))

        with open("relatorio.txt", "w", encoding="utf-8") as f:
            f.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
            f.write(f"{'-' * 70}\n")
            f.write(f"{'Nr.':<5} {'Usuário':<15} {'Espaço utilizado':>10} {'% do uso':>22}\n")

            for x in range(6):
                porcentagem = f"{((armazenamentos[x] / sum(armazenamentos)) * 100):.2f}"
                f.write(f"{(x+1):<5} {(usuarios[x]):<15} {(armazenamentos[x]):>10} MB {(porcentagem):>22}%\n")
    except Exception as e:
        return f"Erro: {e}"

print(analisa_espaco_ocupado("usuarios.txt"))
