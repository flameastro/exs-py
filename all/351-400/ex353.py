# ex353: Escreva um programa em que leia uma sequência de código de operação e valor, onde o código de operação é um inteiro com os seguintes valores
# - `0` (zero): fim
# - `1` (um): inserção
# - `2` (dois): remoção
# O valor lido é um real que deve ser inserido em um vetor (caso a operação seja 1), ou removido do vetor (caso a operação seja 2).
# As inserções no vetor devem ser realizadas de forma que o vetor esteja sempre ordenado.
# No final do programa o vetor resultante deve ser impresso.
# ### Detalhamento:
# - a quantidade máxima de valores que pode ser inserida é 100;
# - se a quantidade máxima for ultrapassada o programa deve dar uma mensagem de erro;
# - se for requisitada a remoção de um número não existente o programa deve dar uma mensagem de erro;
# - se o código de operação for inválido o programa deve continuar lendo um novo código até que ele seja 0 (zero), 1 (um) ou 2 (dois).
# ### Exemplo de execução:
# Entre com operacao (0=fim, 1=insercao, 2=remocao): 1
# Valor: 45.3
# Entre com operacao (0=fim, 1=insercao, 2=remocao): 1
# Valor: 34.3
# Entre com operacao (0=fim, 1=insercao, 2=remocao): 1
# Valor: 40.8
# Entre com operacao (0=fim, 1=insercao, 2=remocao): 2
# Valor: 34.3
# Entre com operacao (0=fim, 1=insercao, 2=remocao): 0
# Vetor resultante
# 40.8 45.3
# Bonus: 3 = mostrar
vetor = []

def verifica_operacao(operacao):
    return operacao in range(0, 4)  # -> operacao == 0/1/2/3?


def adicionar(vetor, elemento):
    tamanho = len(vetor)

    if tamanho == 0:
        novo_vetor = [None] * 1
        novo_vetor[0] = elemento
        return novo_vetor

    novo_vetor = [None] * (tamanho + 1)

    for i in range(len(vetor)):
        novo_vetor[i] = vetor[i]

    novo_vetor[i+1] = elemento
    return novo_vetor




def encontrar(vetor, elemento):
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            return i

    return -1


def remover(vetor, elemento):
    indice = encontrar(vetor, elemento)
    if indice == -1:
        return vetor

    novo_vetor = []

    for i in range(len(vetor)):
        if indice != i:
            novo_vetor.append(vetor[i])

    return novo_vetor


def mostrar(vetor):
    return vetor


while True:
    operacao = int(input("Entre com operacao (0=fim, 1=insercao, 2=remocao, 3=mostrar): "))
    while not verifica_operacao(operacao):
        operacao = int(input("Entre com operacao (0=fim, 1=insercao, 2=remocao, 3=mostrar): "))
        verifica_operacao(operacao)

    if operacao == 0:
        break
    elif operacao == 1:
        valor = float(input("Valor: "))
        vetor = adicionar(vetor, valor)
    elif operacao == 2:
        valor = float(input("Valor: "))
        vetor = remover(vetor, valor)
    elif operacao == 3:
        
        print(mostrar(vetor))
