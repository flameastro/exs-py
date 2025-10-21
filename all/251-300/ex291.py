# ex291: Crie uma função que gere uma cor aleatória em hexadecimal.
import random

def generate_random_color() -> str:
    letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]

    color = ""
    for _ in range(6):
        color += str(random.choice(letters))

    return f"A cor gerada foi: #{color}"


if __name__ == "__main__":
    print(generate_random_color())  # A cor gerada foi: #9284a6
    print(generate_random_color())  # A cor gerada foi: #ca5d9b
    print(generate_random_color())  # A cor gerada foi: #f58480
