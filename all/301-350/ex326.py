# ex326: Você foi contratado por uma loja de venda de livros usados na internet e tem que realizar a simulação do valor de entrega dos pedidos.
# O seu programa deve solicitar ao vendedor o total a ser pago pelo cliente e qual o prazo de entrega desejado (3, 5, 7 ou 10 dias úteis). Para cada tipo de entrega, deve ser criada uma nova função que receba o valor total pago pelo cliente. As entregas disponíveis são as seguintes: 
# 1 - Entrega em 3 dias úteis (adicionar R$ 25,00 reais ao valor pago pelo cliente);
# 2 - Entrega em 5 dias úteis (adicionar R$ 20,00 reais ao valor pago pelo cliente);
# 3 - Entrega em 7 dias úteis (adicionar R$ 15,00 reais ao valor pago pelo cliente) e 
# 4 - Entrega em 10 dias úteis (adicionar R$ 10,00 reais ao valor pago pelo cliente).
def entrega_3_dias(total: float) -> float:
    return f"Valor total: R${round(total + 25, 2)}"


def entrega_5_dias(total: float) -> float:
    return f"Valor total: R${round(total + 20, 2)}"


def entrega_7_dias(total: float) -> float:
    return f"Valor total: R${round(total + 15, 2)}"


def entrega_10_dias(total: float) -> float:
    return f"Valor total: R${round(total + 10, 2)}"


total = round(float(input("Insira o total a ser pago: R$")), 2)

print("PRAZOS DE ENTREGA")
print("1 - Entrega em 3 dias úteis")
print("2 - Entrega em 5 dias úteis")
print("3 - Entrega em 7 dias úteis")
print("4 - Entrega em 10 dias úteis")

prazo = int(input("Qual o prazo de entrega desejado? "))
while prazo not in range(1, 5):
    print("Por favor, selecione um prazo válido")
    prazo = int(input("Qual o prazo de entrega desejado? "))

if prazo == 1:
    print(entrega_3_dias(total))
elif prazo == 2:
    print(entrega_5_dias(total))
elif prazo == 3:
    print(entrega_7_dias(total))
else:
    print(entrega_10_dias(total))
