# ex113: Crie uma função que retorne a soma de todos os valores de um número
def sum_numbers(number: int):
    if number < 1 or number > 10000000:
        return "O número deve estar entre 1 a 10.000.000"

    number_list = []

    for num in str(number):
        number_list.append(int(num))

    sum_numbers = sum(number_list)
    return sum_numbers


if __name__ == "__main__":
    print(sum_numbers(548))  # 5 + 4 + 8 = 17
    print(sum_numbers(77732))  # 7 + 7 + 7 + 3 + 2 = 26
    print(sum_numbers(301))  # 3 + 0 + 1 = 4
