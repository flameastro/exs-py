# ex269: Crie uma classe Mockapi que requisita ao mockapi.io 3 tipos de requisição: o get, o post e o delete.
import requests


class Mockapi:
    def __init__(self, URL):
        self.URL = URL

    def formato(self):
        chaves = ", ".join([chave for chave in requests.get(self.URL).json()[0].keys() if chave != "id"])
        print(f"Você precisará do seguinte formato: {chaves}")


    def get(self):
        print("Requisição GET".center(50, "-"))

        r = requests.get(self.URL)

        if r.status_code == 200:
            print(f"JSON acessado com sucesso\n{r.json()}")

        print(f"Código: {r.status_code}")


    def post(self, data):
        print("Requisição POST".center(50, "-"))

        r = requests.post(self.URL, data)

        if r.status_code == 201:
            print("JSON criado com sucesso!")

        print(f"Código: {r.status_code}")


    def delete(self, user_id):
        print("Requisição DELETE".center(50, "-"))

        if self.URL.endswith("/"):
            self.URL += user_id
        else:
            self.URL += f"/{user_id}"

        r = requests.delete(self.URL)

        if r.status_code == 200:
            print("JSON deletado com sucesso!")
        elif r.status_code == 404:
            print("Este JSON não existe!")

        print(f"Código: {r.status_code}")


if __name__ == "__main__":
    mockapi = Mockapi("https://68c9c972ceef5a150f660771.mockapi.io/name")
    mockapi.formato()
