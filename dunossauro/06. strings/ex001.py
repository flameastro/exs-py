# ex001: Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
string1 = input("String 1: ")
string2 = input("String 2: ")

print("Compara duas strings")
print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Tamanho da String 1: {len(string1)}")
print(f"Tamanho da String 2: {len(string2)}")
if len(string1) == len(string2):
    print("As duas string são de tamanhos iguais.")
else:
    print("As duas string são de tamanhos diferentes.")
    print("As duas string possuem conteúdo diferente.")

if string1 == string2:
    print("As duas strings possuem conteúdo igual.")
