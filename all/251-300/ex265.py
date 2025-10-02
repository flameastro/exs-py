# ex265: Crie uma função que receba uma string como parâmetro e retorne a string fatiada pelos 150 primeiros caracteres e no fim um "Leia Mais" se houver mais que 150 caracteres.
def leia_mais(string):
    return f"{string[:150]} LEIA MAIS..." if len(string) >= 150 else string


if __name__ == "__main__":
    print(leia_mais("""Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos."""))  # Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus dui LEIA MAIS...
    print(leia_mais("Python Test"))  # Python Test
