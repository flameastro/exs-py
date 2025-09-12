# ex167: Crie uma função que recebe uma string como parâmetro e retorne
def remove_espacos(string: str):
    string = string.replace(" ", "")

    return string


if __name__ == "__main__":
    print(remove_espacos("html é uma linguagem de marcação de hipertexto."))  # htmléumalinguagemdemarcaçãodehipertexto.
    print(remove_espacos("brave é um ótimo navegador para segurança."))  # braveéumótimonavegadorparasegurança.
