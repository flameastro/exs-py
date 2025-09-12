# ex126: Crie uma função que: Verifica se um número é primo; Mostra a quantidade de divisores; e quais são eles.
def prime_number(number: int):
    if number < 1 or number > 100000:
        return "The number need to be in a range of 2 and 100000."

    if number == 2:
        return True

    primes = []
    counter = 0
    number_range = range(1, number+1)

    for num in number_range:
        if number % num == 0:
            counter += 1
            primes.append(num)

    return (
    "----------------------------------\n"
    f"Número: {number}\n"
    f"Primo: {counter == 2}\n"
    f"Quant. Divisores: {counter}\n"
    f"Divisores: {primes}"
    "\n----------------------------------\n"
    )

if __name__ == "__main__":
    print(prime_number(16))
    print(prime_number(25))
    print(prime_number(3301))  # Cidada3301!
    print(prime_number(2597))
