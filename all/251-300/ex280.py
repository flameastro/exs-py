# ex280: Crie um programa que peça ao usuário as horas e os minutos do dia e diga quantos segundos já se passaram desde o início do dia (00:00)
horas = int(input("Digite o valor da hora: "))
minutos = int(input("Digite o valor dos minutos: "))

segundos = (minutos * 60) + ((horas * 60) * 60)
print(f"Se passaram {segundos} segundos.")
