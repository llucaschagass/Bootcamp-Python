class ContaBancaria:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor de saque inválido!")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, numero, titular, saldo_inicial=0.0):
        conta = ContaBancaria(numero, titular, saldo_inicial)
        self.contas.append(conta)
        print(f"Conta criada com sucesso! Número da conta: {numero}")

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

# Exemplo de uso do sistema bancário
banco = Banco()

# Criando contas
banco.criar_conta(1, "João Silva", 500.0)
banco.criar_conta(2, "Maria Oliveira", 1000.0)

# Buscando e manipulando uma conta
conta_joao = banco.buscar_conta(1)
if conta_joao:
    conta_joao.consultar_saldo()
    conta_joao.depositar(200.0)
    conta_joao.sacar(100.0)
    conta_joao.consultar_saldo()
else:
    print("Conta não encontrada!")

# Buscando e manipulando outra conta
conta_maria = banco.buscar_conta(2)
if conta_maria:
    conta_maria.consultar_saldo()
    conta_maria.sacar(500.0)
    conta_maria.depositar(150.0)
    conta_maria.consultar_saldo()
else:
    print("Conta não encontrada!")
