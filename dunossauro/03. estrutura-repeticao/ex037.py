# ex037: Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
print(" INSTRUÇÕES ".center(50, "-"))
print("No campo da altura, preencha no formato metro.centimetros (exemplos: 1.65, 1.87, 1.86, 1.84, 2.13)")
print("No campo do peso, preencha no formato quilo.grama (ex: 87.50, 45.3, 125.65, 98.75, 56.75)")
print("Digite \"0\" para sair.")
alturas = []
pesos = []

while True:
    codigo = int(input("Digite o seu código da academia: "))
    if codigo == 0:
        break

    altura = float(input("Digite a sua altura: "))
    peso = float(input("Digite o seu peso: "))

    alturas.append(altura)
    pesos.append(peso)

if len(alturas) != 0:
    mais_alto = max(alturas)
    mais_baixo = min(alturas)
    mais_gordo = max(pesos)
    mais_magro = min(pesos)
    media_alturas = sum(alturas) / len(alturas)

    print(f"O cliente mais alto possui {mais_alto}cm.")
    print(f"O cliente mais baixo possui {mais_baixo}cm.")
    print(f"O cliente mais gordo possui {mais_gordo}kg.")
    print(f"O cliente mais magro possui {mais_magro}kg.")
    print(f"A média das alturas é de {media_alturas}cm.")
    print(f"O peso dos clientes é de: {", ".join([f'{str(peso)}kg' for peso in pesos])}")
else:
    print("Não é possível realizar operações sem dados.")
