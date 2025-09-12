# ex142: Crie uma classe ContaBancaria com atributos titular e saldo, e métodos sacar e depositar.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("O valor do saque é maior que o valor do saldo, não foi possível fazer o saque.")
            return 0

        if valor <= 0:
            print("O valor do saque não pode ser negativo nem nulo.")
            return 0

        self.saldo -= valor
        print("Saque realizado com sucesso.")

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito não pode ser negativo nem nulo.")
            return 0

        self.saldo += valor
        print("Depósito realizado com sucesso.")

    def exibir_saldo(self):
        print(f"O valor do seu saldo é de R${self.saldo}")


if __name__ == "__main__":
    conta1 = ContaBancaria("João", 34500)
    conta1.sacar(560)
    conta1.exibir_saldo()
