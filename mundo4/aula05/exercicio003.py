from random import randint


class ContaBancaria:
    """
    Classe que representa uma conta bancária.
    """

    def __init__(self, id=None, nome="<Desconhecido>", saldo=0):
        self.id = id if id is not None else randint(1000, 9999)
        self.nome = nome
        self.saldo = saldo

        print(f"Conta {self.id} criada com sucesso, saldo atual de R$ {self.saldo:,.2f}")

    def depositar(self, deposito):
        if deposito <= 0:
            print("Valor inválido para depósito.")
            return

        self.saldo += deposito
        print(f"Deposito de {deposito:,.2f} autorizado na conta {self.id}.")

    def sacar(self, saque):
        if saque <= 0:
            print("Valor inválido para saque.")
            return

        if saque > self.saldo:
            print(f"Saque NEGADO de R$ {saque:,.2f} na conta {self.id}: " "SALDO INSUFICIENTE!")
        else:
            self.saldo -= saque
            print(f"Saque de {saque:,.2f} autorizado na conta {self.id}.")

    def __str__(self):
        return f"A conta {self.id} de {self.nome} tem R$ {self.saldo:,.2f} de saldo."


c1 = ContaBancaria(nome="Felippe")
c1.depositar(3500)
c1.sacar(3000)
print(c1)
