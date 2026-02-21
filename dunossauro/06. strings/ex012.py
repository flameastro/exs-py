# ex012: Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133
def corrigir_telefone():
    print("Valida e corrige número de telefone")

    telefone = input("Telefone: ").strip()
    telefone_sem_traco = telefone.replace("-", "")

    if not telefone_sem_traco.isdigit():
        print("Número inválido! Digite apenas números e, opcionalmente, o traço.")
        return

    tamanho = len(telefone_sem_traco)

    if tamanho == 8:
        print("Telefone com 8 dígitos. Nenhuma correção necessária.")
        telefone_corrigido = telefone_sem_traco
    elif tamanho == 7:
        print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
        telefone_corrigido = "3" + telefone_sem_traco
    else:
        print("Número de telefone inválido! Deve ter 7 ou 8 dígitos.")
        return

    print("Telefone corrigido sem formatação:", telefone_corrigido)
    print("Telefone corrigido com formatação:", telefone_corrigido[:4] + "-" + telefone_corrigido[4:])

corrigir_telefone()
