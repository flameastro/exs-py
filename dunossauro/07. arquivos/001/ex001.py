# ex001: Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:

# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:

# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4

# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

def valida_ips(arquivo: str):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            f.seek(0)

            invalidos = []
            validos = []
            IPs = [x.removesuffix('\n') for x in f.readlines()]
            for x in IPs:
                invalido = False
                ip = x.split('.')
                for octal in ip:
                    if int(octal) > 255:
                        invalido = True

                if invalido:
                    invalidos.append(x)
                else:
                    validos.append(x)

        print(validos, invalidos)
        with open("relatorio.txt", "w", encoding="utf-8") as f:
            f.write("IPS VÁLIDOS\n")
            for x in validos:
                f.write(f"{x}\n")

            f.write("\nIPS INVÁLIDOS\n")
            for x in invalidos:
                f.write(f"{x}\n")

        return "Cheque o arquivo relatorio.txt!"
    except Exception as e:
        return f"Erro: {e}"


valida_ips("lista-ips.txt")
