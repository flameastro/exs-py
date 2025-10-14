# ex283: Crie um algoritmo que peça ao usuário uma palavra e exiba o seguinte resultado:
# palavra: SONHO
# SONHO
# SONHO SONHO
# SONHO SONHO SONHO
# SONHO SONHO SONHO SONHO
# SONHO SONHO SONHO SONHO SONHO
palavra = input("Digite uma palavra: ").strip()

for i in range(1, 6):
    print(f"{palavra} " * i)
