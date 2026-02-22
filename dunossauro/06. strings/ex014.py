# ex014: Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
def leet_speak(texto):
    leet = {
        'a': '4', 'b': '8', 'c': '(', 'd': '|)', 'e': '3',
        'f': 'ph', 'g': '6', 'h': '#', 'i': '1', 'j': '_|',
        'k': '|<', 'l': '1', 'm': '/\\/\\', 'n': '|\\|', 'o': '0',
        'p': '|2', 'q': '0_', 'r': '|2', 's': '5', 't': '7',
        'u': '|_|', 'v': '\\/', 'w': '\\/\\/', 'x': '><', 'y': '`/',
        'z': '2'
    }

    resultado = ""
    for letra in texto.lower():
        resultado += leet.get(letra, letra)
    return resultado

texto = input("Digite um texto: ")
print("Texto em leet speak:", leet_speak(texto))
