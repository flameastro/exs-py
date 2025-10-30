# ex023: A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

# usuarios.txt
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres.

# A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

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
def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def percentual_uso(espaco, total):
    return (espaco / total) * 100

usuarios = []
with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        nome = linha[:15].strip()
        espaco = int(linha[15:].strip())
        usuarios.append((nome, espaco))

total_espaco = sum(espaco for _, espaco in usuarios)
usuarios_mb = [(nome, bytes_para_mb(espaco)) for nome, espaco in usuarios]

with open("relatorio.txt", "w") as rel:
    rel.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    rel.write("------------------------------------------------------------------------\n")
    rel.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")

    for i, (nome, espaco_mb) in enumerate(usuarios_mb, start=1):
        rel.write(f"{i:<4} {nome:<15} {espaco_mb:10.2f} MB {percentual_uso(espaco_mb, bytes_para_mb(total_espaco)):14.2f}%\n")

    rel.write(f"\nEspaço total ocupado: {bytes_para_mb(total_espaco):.2f} MB\n")
    rel.write(f"Espaço médio ocupado: {bytes_para_mb(total_espaco)/len(usuarios):.2f} MB\n")
