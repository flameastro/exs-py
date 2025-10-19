# ex016: A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
termos = []
termo = 1
i = 0

while True:
    if len(termos) != 0:
        termo = termo + int(termos[i-1])
    else:
        termos.append(str(termo))
    termos.append(str(termo))

    if termo >= 500:
        break

    i += 1

print(f"Termos: {",".join(termos)}")
