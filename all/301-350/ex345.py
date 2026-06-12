# ex345: Crie uma função que receba um valor em horas como parâmetro no formato HH:MM:SS e retorne a soma dos segundos das horas, minutos e segundos
def time_conversor(hour):
    hour = hour.split(":")
    return (int(hour[0]) * 3600) + (int(hour[1]) * 60) + int(hour[2])

if __name__ == "__main__":
    print(time_conversor("16:04:33"))
    print(time_conversor("01:00:00"))
    print(time_conversor("12:54:32"))
