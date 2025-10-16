# ex003: Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino
# M - Masculino
# Sexo Inválido.
letra = input("Digite o seu gênero (M/F): ")

if letra == "M":
    print("Masculino")
elif letra == "F":
    print("Feminino")
else:
    print("Sexo inválido")
