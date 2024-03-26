class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente.')

    def verificar_saldo(self):
        print(f'Saldo disponível: R${self.saldo}')

# Exemplo de uso da classe ContaBancaria
if __name__ == "__main__":
    conta = ContaBancaria("Fulano", 1000)
    conta.verificar_saldo()
    conta.depositar(500)
    conta.verificar_saldo()
    conta.sacar(200)
    conta.verificar_saldo()
    conta.sacar(2000)
