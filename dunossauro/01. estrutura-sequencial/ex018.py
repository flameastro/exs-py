# ex018: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_link = float(input("Digite a velocidade da internet (em Mbps): "))
tempo_minutos = (tamanho_arquivo * 8) / (velocidade_link * 60)

print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")
