# ex012: Faça uma classe ContaInvestimento que seja semelhante a classe ContaBancaria, com a diferença de que se adicione um atributo taxa_juros. Forneça um inicializador que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicione_juros() (sem parâmetro explícito) que adicione juros à conta.

# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicione_juros() cinco vezes e imprime o saldo resultante.
class ContaInvestimento:
    def __init__(self, numero: int, nome: str, taxa_juros: float, saldo: float = 0):
        self.numero = numero
        self.nome = nome
        self.taxa_juros = taxa_juros
        self.saldo = saldo

    def alterar_nome(self, novo_nome: str):
        self.nome = novo_nome
        return "Nome alterado com sucesso."

    def realizar_deposito(self, valor: float):
        if valor > 0:
            self.saldo += valor
            return "Depósito realizado com sucesso!"
        return "O depósito não pode ter sido efetuado. Modifique o valor e tente novamente."

    def realizar_saque(self, valor: float):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return "Saque efetuado com sucesso!"
        return "O saque não pode ter sido efetuado. Modifique o valor e tente novamente."

    def ver_saldo(self):
        return self.saldo

    def adicione_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        print(f"Juros aplicados! Novo saldo: R${self.saldo:.2f}")


if __name__ == "__main__":
    poupanca = ContaInvestimento(1, "Poupança", 0.10, 1000.00)

    for _ in range(5):
        poupanca.adicione_juros()

    print(f"Saldo final após 5 aplicações de juros: R${poupanca.ver_saldo():.2f}")
