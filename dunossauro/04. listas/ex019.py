# ex019: Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
print("Qual o melhor Sistema Operacional para uso em servidores?")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- MacOS")
print("6- Outro")

SOs = ["Windows Server", "Unix", "Linux", "Netware", "MacOS", "Outro"]
votos = [0] * 6

while True:
    sistema_operacional = int(input("Escolha o sistema operacional (1-6) ou 0 para encerrar: "))

    if sistema_operacional == 0:
        break
    elif 1 <= sistema_operacional <= 6:
        votos[sistema_operacional - 1] += 1
    else:
        print("Valor inválido! Digite um número entre 0 e 6.")

total_votos = sum(votos)

print("\nSistema Operacional     Votos   %")
print("-" * 35)
for i in range(6):
    percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
    print(f"{SOs[i]:<22} {votos[i]:<7} {percentual:.2f}%")

print("-" * 35)
print(f"Total de votos: {total_votos}")

mais_votado = max(votos)
indice_vencedor = votos.index(mais_votado)
percentual_vencedor = (mais_votado / total_votos) * 100 if total_votos > 0 else 0

print(f"\nO Sistema Operacional mais votado foi o {SOs[indice_vencedor]}, "
      f"com {mais_votado} votos, correspondendo a {percentual_vencedor:.2f}% dos votos.")
