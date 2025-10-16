# ex008: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
produto1 = float(input("Informe o primeiro produto: "))
produto2 = float(input("Informe o segundo produto: "))
produto3 = float(input("Informe o terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"Você deve comprar o primeiro produto -> {produto1}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"Você deve comprar o segundo produto -> {produto2}")
elif produto3 < produto1 and produto3 < produto2:
    print(f"Você deve comprar o terceiro produto -> {produto3}")
else:
    if produto1 == produto2 and produto1 == produto3:
        print(f"Todos são iguais -> {produto1}")
    elif produto1 == produto2:
        print(f"Ambos o primeiro e o segundo produto são iguais -> {produto1}")
    elif produto2 == produto3:
        print(f"Ambos o segundo e o terceiro produto são iguais -> {produto2}")
    elif produto1 == produto3:
        print(f"Ambos o primeiro e o terceiro produto são iguais -> {produto1}")
