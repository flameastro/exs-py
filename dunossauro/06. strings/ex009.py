# ex009: Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através dos caracteres de formatação.
CPF = input("Insira um CPF no formato xxx.xxx.xxx-xx: ")

if CPF.count("-") != 1 or len(CPF) != 14:
    print("❌ CPF Inválido.")
else:
    CPF = CPF.split(".")
    CPF = CPF + CPF[2].split("-")
    del CPF[2]

    inicio = CPF[0]
    primeiro_meio = CPF[1]
    segundo_meio = CPF[2]
    fim = CPF[3]

    if len(inicio) == 3 and len(primeiro_meio) == 3 and len(segundo_meio) == 3 and len(fim) == 2:
        print("✅ CPF válido.")
    else:
        print("❌ CPF Inválido.")
