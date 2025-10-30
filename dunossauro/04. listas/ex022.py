# ex022: Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:

# necessita da esfera;
# necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
# Ao final o programa deverá emitir o seguinte relatório:

# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%
total = 0
defeitos = [0, 0, 0, 0]

while True:
    identificacao = int(input("Número de identificação do mouse (0 para encerrar): "))
    if identificacao == 0:
        break

    print("Tipos de defeito:")
    print("1- necessita da esfera")
    print("2- necessita de limpeza")
    print("3- necessita troca do cabo ou conector")
    print("4- quebrado ou inutilizado")
    tipo = int(input("Informe o tipo de defeito: "))

    if 1 <= tipo <= 4:
        defeitos[tipo - 1] += 1
        total += 1
    print()

print(f"\nQuantidade de mouses: {total}\n")
print("Situação".ljust(35), "Quantidade".ljust(15), "Percentual")
print(f"1- necessita da esfera".ljust(35), f"{defeitos[0]}".ljust(15), f"{(defeitos[0]/total)*100:.0f}%")
print(f"2- necessita de limpeza".ljust(35), f"{defeitos[1]}".ljust(15), f"{(defeitos[1]/total)*100:.0f}%")
print(f"3- necessita troca do cabo ou conector".ljust(35), f"{defeitos[2]}".ljust(15), f"{(defeitos[2]/total)*100:.0f}%")
print(f"4- quebrado ou inutilizado".ljust(35), f"{defeitos[3]}".ljust(15), f"{(defeitos[3]/total)*100:.0f}%")
