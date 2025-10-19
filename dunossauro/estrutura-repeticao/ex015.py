# ex015: A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
quantidade = int(input("Digite o n-ésimo termo: "))
termos = []
termo = 1

for i in range(0, quantidade+1):
    if len(termos) != 0:
        termo = termo + int(termos[i-1])
    else:
        termos.append(str(termo))
    termos.append(str(termo))

print(f"Termos: {",".join(termos)}")
