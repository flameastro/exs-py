# ex242: Formatar CPF: Peça um CPF (apenas números) e formate-o como XXX.XXX.XXX-XX.
def formata_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


if __name__ == "__main__":
    print(formata_cpf("12345678900"))  # 123.456.789-00
    print(formata_cpf("67489326455"))  # 674.893.264-55
    print(formata_cpf("88976325373"))  # 889.763.253-73
