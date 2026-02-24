# ex005: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:
    def __init__(self, numero: int, nome: str, saldo: float = 0):
        self.numero = numero
        self.nome = nome
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


if __name__ == "__main__":
    cc1 = ContaCorrente(87467, "Gustavo Pinheiro", 34653.79)
    print(cc1.realizar_deposito(4500))  # Depósito realizado com sucesso!
    print(cc1.ver_saldo())  # 39153.79

    cc2 = ContaCorrente(9483, "Maria Peixoto", 76554.67)
    print(cc2.realizar_saque(50000))  # Saque efetuado com sucesso!
    print(cc2.ver_saldo())  # 26554.67
