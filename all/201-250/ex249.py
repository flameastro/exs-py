# ex249: Crie um programa para contagem regressiva para lançamento de foguete de 10 a 0
from time import sleep

# i = 10
# while i >= 1:
#     print(f"{i}...")
#     sleep(1)
#     i -= 1
# print("Lançar!!!")

for i in range(10, 0, -1):
    print(f"{i}...")
    sleep(1)
print("Lançar!!!")
