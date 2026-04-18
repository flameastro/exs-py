# ex338: Prepare um algoritmo que permita a entrada de um número n (inteiro) e, então, o converta ao sistema binário, armazenando o resultado em um vetor de tamanho máximo 16. O algoritmo deverá testar, primeiro, se o número não ultrapassa 32.768, que é o maior inteiro que se pode representar com 16 bits (o tamanho do vetor). Depois, o conteúdo desse vetor deve ser exibido na tela.
n = int(input("Digite o número: "))
numero = n
binario = []

if n > 0:
    if n >= 32768:
        print("Você inseriu um valor muito alto")
    else:
        while n != 0:
            binario.append(n % 2)
            n //= 2

        binario.reverse()
        print(f"O número {numero} convertido em binário é: {binario}")
elif n < 0:
    print("Insira um valor válido")
else:
    binario.append(0)
    print(f"O número 0 convertido em binário é: {binario}")
