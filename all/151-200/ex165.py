# ex165: Nathan ama ciclismo. Porque Nathan sabe que é importante se manter hidratado. Ele toma 0.5 litros de água para cada hora de ciclismo. Você recebeu o tempo em horas e precisa retornar o número de litros que Nathan tomou, arredondado.
def litros_agua(horas: float) -> int:
    litros_hora = 0.5

    litros = int(horas * litros_hora)
    return litros


if __name__ == "__main__":
    print(litros_agua(3))  # 1
    print(litros_agua(6.7))  # 3
    print(litros_agua(11.8))  # 5
    print(litros_agua(15))  # 7
